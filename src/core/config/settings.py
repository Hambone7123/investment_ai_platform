import os
from dataclasses import dataclass

@dataclass
class Settings:
    """
    Central configuration for the Investment AI Platform.
    """

    # AI Provider
    ai_provider: str = "gemini"   # gemini | openai | claude | local
    model_name: str = "gemini-1.5-pro"

    # Paths (Google Drive mounted in Colab)
    project_root: str = "/content/drive/MyDrive/Investment_AI_Platform"

    data_dir: str = "/content/drive/MyDrive/Investment_AI_Platform/data"
    output_dir: str = "/content/drive/MyDrive/Investment_AI_Platform/outputs"
    logs_dir: str = "/content/drive/MyDrive/Investment_AI_Platform/logs"

    # Model behavior
    temperature: float = 0.3
    max_tokens: int = 4096

    # Debugging
    debug: bool = True


def get_settings() -> Settings:
    return Settings()
