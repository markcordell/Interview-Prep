from prompts import USER_REQUEST_PROMPT_V1


def generate_user_request_prompt(user_request: str) -> str:
    return USER_REQUEST_PROMPT_V1 + user_request + "\n"
