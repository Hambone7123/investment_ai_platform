from abc import ABC, abstractmethod

class BaseLLM(ABC):
    """
    Abstract interface for all AI models.
    (Gemini, OpenAI, Claude, local models)
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass
