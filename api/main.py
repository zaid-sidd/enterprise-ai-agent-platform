import logging

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from google.genai import types
from google.genai import errors as genai_errors

from src.utils.logging import setup_logging

from src.agent.graph import build_graph
from src.agent.memory import load_conversation_messages

from src.db.repository import (
    create_conversation,
    add_message,
    add_tool_call,
    conversation_exists,
)


setup_logging()

logger = logging.getLogger(__name__)


class ChatRequest(BaseModel):
    message: str = Field(
        min_length=1,
        max_length=2000,
    )
    conversation_id: int | None = None


app = FastAPI(
    title="Enterprise AI Agent Platform",
    version="1.0.0",
)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post("/agent/chat")
def chat(request: ChatRequest):

    try:

        logger.info(
            "Chat request received | conversation_id=%s",
            request.conversation_id,
        )

        if request.conversation_id is None:

            conversation_id = create_conversation()
            history = []

        else:

            conversation_id = request.conversation_id

            if not conversation_exists(
                conversation_id
            ):
                raise HTTPException(
                    status_code=404,
                    detail="Conversation not found.",
                )

            history = load_conversation_messages(
                conversation_id
            )

        logger.info(
            "Using conversation | conversation_id=%s",
            conversation_id,
        )

        add_message(
            conversation_id,
            "user",
            request.message,
        )

        history.append(
            types.Content(
                role="user",
                parts=[
                    types.Part(
                        text=request.message
                    )
                ],
            )
        )

        graph = build_graph()

        initial_state = {
            "conversation_id": conversation_id,
            "messages": history,
            "tool_calls": [],
            "tool_results": [],
        }

        logger.info(
            "Starting agent execution | conversation_id=%s",
            conversation_id,
        )

        result = graph.invoke(initial_state)

        for tool_call, tool_result in zip(
            result["tool_calls"],
            result["tool_results"],
        ):

            add_tool_call(
                conversation_id=conversation_id,
                tool_name=tool_call["name"],
                arguments=tool_call["arguments"],
                result=tool_result["result"],
            )

            logger.info(
                "Tool executed | conversation_id=%s | tool=%s",
                conversation_id,
                tool_call["name"],
            )

        final_message = result["messages"][-1]

        final_text = ""

        for part in final_message.parts:

            if getattr(part, "text", None):
                final_text += part.text

        add_message(
            conversation_id,
            "assistant",
            final_text,
        )

        logger.info(
            "Agent response generated | conversation_id=%s",
            conversation_id,
        )

        return {
            "conversation_id": conversation_id,
            "response": final_text,
            "tool_calls": result["tool_calls"],
        }

    except HTTPException:
        raise

    except genai_errors.ClientError as exc:

        if getattr(exc, "code", None) == 429:

            logger.error(
                "Gemini quota exhausted | conversation_id=%s | error=%s",
                request.conversation_id,
                exc,
            )

            raise HTTPException(
                status_code=429,
                detail="AI service quota has been exhausted. Please try again later.",
            ) from exc

        raise HTTPException(
            status_code=500,
            detail="AI service request failed.",
        ) from exc    

    except genai_errors.ServerError as exc:
        
        logger.error(
            "Gemini service unavailable | conversation_id=%s | error=%s",
            request.conversation_id,
            exc,
        )

        raise HTTPException(
            status_code=503,
            detail="AI service is temporarily unavailable. Please try again.",
        ) from exc

    except Exception as exc:

        logger.exception(
            "Unexpected error | conversation_id=%s",
            request.conversation_id,
        )

        raise HTTPException(
            status_code=500,
            detail="Unable to process the request.",
        ) from exc