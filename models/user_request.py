from prompt import Prompt
from prompts import USER_REQUEST_SNIPPET


def generate_user_request_prompt(user_request: str) -> Prompt:
    return USER_REQUEST_SNIPPET + user_request

    return USER_REQUEST_PROMPT_V1 + user_request + "\n"
