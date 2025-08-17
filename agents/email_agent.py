from dotenv import load_dotenv
from agents.base_agent import BaseAgent

load_dotenv()


class EmailAgent(BaseAgent):
    def __init__(self):
        base_prompt = """
            You are an email agent that helps users create and send emails.
        """

        super().__init__(llm=None, prompt=base_prompt)
