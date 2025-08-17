"""
This module defines the BaseAgent class, which serves as a template for creating agents.
"""

from crewai import LLM
from common.config import Config
from common.logging import setup_logger
from datetime import date as Date


class BaseAgent:
    """
    This class serves as a base class for agents, providing a structure for initialization and prompt handling.
    """

    def __init__(self, llm: str | None, prompt: str):
        self.logger = setup_logger(
            name=self.__class__.__name__,
            log_level=Config.constants.DEFAULT_LOGGING_LEVEL,
            log_file=Config.constants.LOG_DIRECTORY
            / (Date.today().strftime("%Y-%m-%d") + ".log"),
        )

        llm = Config.constants.GEMINI_MODEL if llm is None else llm

        self.llm = LLM(
            model=llm,
            temperate=Config.constants.DEFAULT_TEMPERATE,
            api_key=Config.constants.GEMINI_API_KEY,
            max_completion_tokens=Config.constants.MAX_COMPLETION_TOKENS,
        )

    def invoke(self, user_prompt: str):
        agent_response = self.llm.call(user_prompt)
        self.logger.info(f"Agent {self.__class__.__name__} response: {agent_response}")
        return agent_response
