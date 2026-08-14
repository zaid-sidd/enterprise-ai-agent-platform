# Enterprise AI Agent Platform

A hands-on project for building an AI agent that can understand user requests, decide when a tool is needed, execute the tool, and use the result to generate a response.

The project is being built step by step to understand how agentic AI systems work behind the scenes rather than relying entirely on ready-made frameworks.

## Current Architecture

User
 ↓
LangGraph Agent
 ↓
Tool Selection
 ↓
Tool Execution
 ├── Calculator
 └── Employee Information
 ↓
Agent
 ↓
Final Response

## Current Capabilities

- Gemini LLM integration
- Function / tool calling
- Multiple tools
- Generic tool registry
- Tool execution
- LangGraph state management
- Conditional routing
- Multi-tool agent workflow

## Tech Stack

- Python
- Google Gemini API
- LangGraph
- LangChain Core
- Git / GitHub

## Current Status

### Completed
- Gemini integration
- Calculator and employee information tools
- Generic tool registry and executor
- LangGraph agent workflow
- Multi-tool execution

### Planned
- PostgreSQL persistence
- Redis
- FastAPI backend
- Error handling and retries
- Logging and observability
- Docker Compose
- Testing and evaluation

## Project Structure

enterprise-ai-agent-platform/
├── src/
│   ├── agent/
│   ├── tools/
│   ├── config.py
│   └── llm.py
├── test_*.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

## Running the Project

Create and activate the virtual environment:

python3 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Create a .env file with:

GOOGLE_API_KEY=your_api_key

Run the current agent:

python test_langgraph_agent.py

## About

This project focuses on understanding the engineering behind agentic AI systems, including tool calling, agent state, conditional workflows, and multi-tool execution. The system is being developed incrementally, with each major component tested before moving to the next stage.