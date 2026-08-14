from google.genai import types

from src.llm import GeminiLLM
from src.tools.executor import execute_tool


def main():

    llm = GeminiLLM()

    user_question = "What is 25 * 4 + 10?"

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part(
                    text=user_question
                )
            ],
        )
    ]

    # Step 1: Ask LLM
    response = llm.generate_with_tools(contents)

    function_call = response.candidates[0].content.parts[0].function_call

    print("\nTOOL REQUEST")
    print("Tool:", function_call.name)
    print("Arguments:", dict(function_call.args))

    # Step 2: Execute tool
    tool_result = execute_tool(
        function_call.name,
        dict(function_call.args),
    )

    print("\nTOOL RESULT")
    print(tool_result)

    # Step 3: Send result back to LLM
    contents.append(response.candidates[0].content)

    contents.append(
        types.Content(
            role="user",
            parts=[
                types.Part.from_function_response(
                    name=function_call.name,
                    response={
                        "result": tool_result
                    },
                )
            ],
        )
    )

    # Step 4: Generate final answer
    final_response = llm.generate_with_tools(contents)

    print("\nFINAL ANSWER")
    print(final_response.text)


if __name__ == "__main__":
    main()
