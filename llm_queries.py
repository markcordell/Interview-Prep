from turtle import st
from typing import Optional, List, Callable, Type
import openai

from models.problems import SeenProblems
from models.user_info import UserInfo

GPT_MODEL = "gpt-4"


class LLMQuerier:
    def query(system_prompt: str, user_prompt: Optional[str] = None) -> str:
        raise NotImplementedError


# This is the base level GPT query system. This should only be used to create new LLMQuery
class GPT4(LLMQuerier):
    def query(system_prompt: str, user_prompt: Optional[str] = None) -> str:
        messages = [{"role": "system", "content": system_prompt}]
        if user_prompt:
            messages.append({"role": "user", "content": user_prompt})

        response = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=messages,
            temperature=1,
            max_tokens=1024,
            presence_penalty=1.02,
            stop="[STOP]",
        )

        return response.choices[0].message.content


def query_generate_interview_question(
    query_agent: Type[LLMQuerier],
    seen_problems: List[SeenProblems],
    initial_prompt: str,
    user_information: UserInfo,
    user_request: Optional[str],
) -> str:
    if not user_request:
        user_request = ""

    # Starts our seen problems prompt section with header
    formatted_problems = "Seen Problems:\n"

    for problem in seen_problems:
        # Add a starting and ending set of triple quotes
        # Helps the model determine when a problem starts and ends
        formatted_problems += "```\n"
        formatted_problems += f"{problem.problem}\n"
        formatted_problems += "```\n"

    final_prompt = (
        initial_prompt
        + user_request
        + user_information.generate_prompt()
        + formatted_problems
    )

    return query_agent.query(system_prompt=final_prompt)
