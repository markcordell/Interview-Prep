from typing import List
from prompt import Prompt
from prompts import USER_REQUEST_PROMPT_V1


class UserInfo:
    interview_type: str
    seniority: str
    years_of_experience: float
    preferred_programming_language: str
    topics_to_avoid: List[str]

    def __init__(
        self,
        interview_type: str,
        seniority: str,
        years_of_experience: float,
        preferred_programming_language: str,
        topics_to_avoid: List[str],
    ) -> None:
        self.interview_type = interview_type
        self.seniority = seniority
        self.years_of_experience = years_of_experience
        self.preferred_programming_language = preferred_programming_language
        self.topics_to_avoid = topics_to_avoid

    def generate_prompt(self) -> Prompt:
        """
        Generates a prompt of the user information in a human/LLM readable format
        """
        user_info = Prompt("User Information:")

        for key, value in self.__dict__.items():
            formatted_key = key.title().replace("_", " ")
            user_info += f"{formatted_key}: {value}"
        return user_info

    def __repr__(self) -> str:
        return str(self.generate_prompt())

    def __str__(self) -> str:
        return str(self.generate_prompt())
