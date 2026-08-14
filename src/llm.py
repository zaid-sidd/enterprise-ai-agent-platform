from google import genai
from google.genai import types

from src.config import GOOGLE_API_KEY
from src.tools.tool_registry import TOOL_DEFINITIONS


class GeminiLLM:

    def __init__(self):
        self.client = genai.Client(
            api_key=GOOGLE_API_KEY
        )

    def generate_with_tools(self, contents):

        function_declarations = [
            types.FunctionDeclaration(
                name=tool["name"],
                description=tool["description"],
                parameters=tool["parameters"],
            )
            for tool in TOOL_DEFINITIONS
        ]

        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=contents,
            config=types.GenerateContentConfig(
                tools=[
                    types.Tool(
                        function_declarations=function_declarations
                    )
                ]
            ),
        )

        return response