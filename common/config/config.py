import os
from pathlib import Path
from typing import Literal

from dotenv import load_dotenv

load_dotenv()


class _Constants:
    PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]
    GEMINI_MODEL: str = "gemini/gemini-2.5-flash"
    GEMINI_API_KEY: str = os.getenv("GEMINI_AI_API_KEY", "")
    DEFAULT_TEMPERATE: float = 0.1
    MAX_COMPLETION_TOKENS = 2**7
    DEFAULT_LOGGING_LEVEL: Literal["INFO", "ERROR", "WARNING", "CRITICAL"] = "INFO"
    LOG_DIRECTORY: Path = PROJECT_ROOT / "logs"


class Config:
    constants: _Constants = _Constants()
