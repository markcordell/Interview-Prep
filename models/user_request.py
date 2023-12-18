from prompt import Prompt
from prompts import USER_REQUEST_PROMPT


def generate_user_request_prompt(user_request: str) -> Prompt:
    return USER_REQUEST_PROMPT + user_request
