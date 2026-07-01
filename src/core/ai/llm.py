from .gemini_provider import GeminiProvider

class LLM:

    def __init__(self, provider: str, api_key: str):
        self.provider = provider

        if provider == "gemini":
            self.model = GeminiProvider(api_key)

        else:
            raise ValueError(f"Provider not supported yet: {provider}")

    def generate(self, prompt: str) -> str:
        return self.model.generate(prompt)
