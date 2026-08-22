# Enterprise AI Agent Platform

A hands-on project built to understand how an AI agent works in a real application instead of treating an LLM as just a chatbot.

The agent can understand a user's request, decide when a tool is required, execute the tool, maintain conversation history, and generate a final response. The project also includes persistent storage, Redis caching, an API layer, error handling, logging, automated tests, and Docker-based deployment.

## Features

- Natural language interaction through a REST API
- LLM-powered agent using Google Gemini
- LangGraph-based agent workflow
- Tool selection and execution
- Calculator tool
- Employee information tool
- Multi-turn conversations
- Persistent conversation history
- Tool-call persistence
- PostgreSQL database
- Redis-based conversation caching
- Request validation
- Structured application logging
- API error handling
- Automated API tests with Pytest
- Dockerized FastAPI application
- Docker Compose setup for FastAPI, PostgreSQL, and Redis

## Architecture

```text
                         Client
                           |
                           v
                    +--------------+
                    |   FastAPI    |
                    +------+-------+
                           |
                           v
                    +--------------+
                    |  LangGraph   |
                    |    Agent     |
                    +------+-------+
                           |
                           v
                    +--------------+
                    | Gemini LLM   |
                    +------+-------+
                           |
                    Tool Selection
                           |
                 +---------+---------+
                 |                   |
                 v                   v
          +-------------+     +-------------+
          | Calculator  |     |  Employee   |
          |    Tool     |     | Information |
          +-------------+     +-------------+
                 |
                 v
          +-------------------------------+
          |       Data & Memory Layer     |
          |                               |
          |  PostgreSQL   +    Redis      |
          |  - Messages        - Cache    |
          |  - Conversations              |
          |  - Tool Calls                 |
          +-------------------------------+
```
## Tech Stack

- Python
- FastAPI
- LangGraph
- Google Gemini API
- PostgreSQL
- Redis
- Docker
- Docker Compose
- Pytest

## Project Structure
```text
enterprise-ai-agent-platform/
│
├── api/
│   ├── __init__.py
│   └── main.py
│
├── src/
│   ├── agent/
│   │   ├── graph.py
│   │   ├── memory.py
│   │   ├── nodes.py
│   │   ├── router.py
│   │   └── state.py
│   │
│   ├── db/
│   │   ├── cache.py
│   │   ├── connection.py
│   │   ├── redis_client.py
│   │   ├── repository.py
│   │   └── schema.sql
│   │
│   ├── tools/
│   │   ├── calculator.py
│   │   ├── employee.py
│   │   ├── executor.py
│   │   └── tool_registry.py
│   │
│   ├── config.py
│   └── utils/
│       └── logging.py
│
├── tests/
│   ├── test_api_errors.py
│   ├── test_api_validation.py
│   ├── test_health.py
│   └── manual/
│
├── Dockerfile
├── docker-compose.yml
├── pytest.ini
├── requirements.txt
├── .env.example
├── .gitignore
├── .dockerignore
└── README.md
```
## Running the Project

### 1. Configure the environment

Create a `.env` file in the project root using .env.example as a reference.

Add your Gemini API key:

```text
GOOGLE_API_KEY=your_google_api_key_here
```

The .env file is excluded from Git.

### 2. Start the application

From the project root:
```bash
docker compose up -d --build
```

Check the running containers:
```bash
docker compose ps
```

The stack contains:
- FastAPI
- PostgreSQL
- Redis

### 3. Check the API

Open the Swagger documentation:
```text
http://localhost:8000/docs
```

Health check:
```text
http://localhost:8000/health
```

Expected response:

```json
{
  "status": "ok"
}
```

## Example

The main endpoint is:
```text
POST /agent/chat
```

Example request:
```json
{
  "message": "What is 25 * 4 + 10?"
}
```

The agent identifies that the calculator tool is required, executes it, and returns the result.

Example response:
```json
{
  "conversation_id": 61,
  "response": "25 * 4 + 10 is 110.",
  "tool_calls": [
    {
      "name": "calculate",
      "arguments": {
        "expression": "25 * 4 + 10"
      }
    }
  ]
}
```

Conversation and tool-call information are persisted in PostgreSQL, while Redis is used for conversation caching.

## Conversation Memory

The application supports multi-turn conversations using a conversation ID.

Previous messages are loaded from persistent storage and provided to the agent as conversation context.

PostgreSQL stores conversations, messages, and tool calls. Redis is used as a cache for conversation history.

## Error Handling

The API handles common failure scenarios:

- 422 — Invalid request data
- 404 — Conversation not found
- 429 — Gemini quota exhausted
- 503 — Gemini service temporarily unavailable
- 500 — Unexpected application error

Application events and errors are logged using Python's built-in logging module.

## Testing

Automated API tests are located under tests/.

Run the complete test suite:
```bash
pytest -v
```

The test suite covers:
- Health endpoint
- Request validation
- Invalid conversation handling
- Gemini quota error handling
- Gemini service error handling
- Unexpected application errors

Manual component-level tests used during development are kept under:
```text
tests/manual/
```

## Docker

The complete application runs through Docker Compose using three services:
```text
+---------------------------------------------+
|              Docker Compose                 |
|                                             |
|  +-----------+   +------------+             |
|  |  FastAPI  |   | PostgreSQL |             |
|  |   :8000   |   |   :5432    |             |
|  +-----------+   +------------+             |
|        |                                    |
|        +-------------+                      |
|                      |                      |
|                 +----------+                |
|                 |  Redis   |                |
|                 |  :6379   |                |
|                 +----------+                |
+---------------------------------------------+
```
FastAPI communicates with PostgreSQL and Redis through Docker Compose service names.

## Why I Built This

The main goal of this project was to understand agentic AI from the application side.

Instead of only making an LLM API call, the project explores how an AI agent can work with tools, maintain state, persist conversations, use caching, expose functionality through an API, and run as a containerized application.

The project was built incrementally, with individual components tested first and then combined into a complete working system.

## Future Improvements
- Authentication and authorization
- Additional enterprise tools
- Streaming responses
- Background task processing
- Observability and metrics
- CI/CD
- Production cloud deployment