from src.llm import GeminiLLM


llm = GeminiLLM()

response = llm.generate_with_tools(
    "What is 25 * 4 + 10? Use the calculator tool."
)

print(response)
