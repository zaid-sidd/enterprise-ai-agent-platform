from src.llm import GeminiLLM


llm = GeminiLLM()

answer = llm.generate(
    "Explain what an AI agent is in one simple sentence."
)

print(answer)
