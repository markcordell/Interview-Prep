from email.policy import default
from typing import List, Optional
from prompts import CODING_INTERVIEW_PROMPT_V1
from models.UserInfo import UserInfo, generate_user_request_prompt
from models.problems import load_seen_problems, SeenProblems
from prompt_generator import query_generate_interview_question

import click


FILES_DIR = "./seen_problems"


@click.command()
@click.option(
    "--user-request",
    default=None,
    help="Make a request for the interview question (I.E. Make it a graph problem))",
)
def generate_question(user_request: Optional[str]):
    user_info = UserInfo(
        interview_type="Backend",
        seniority="Senior",
        years_of_experience=6,
        preferred_programming_language="Python3",
        topics_to_avoid="Levenshtein Distance",
    )
    seen_problems = load_seen_problems(FILES_DIR)

    parsed_user_request = generate_user_request_prompt(user_request)
    # TODO: Pass user_request to this function
    LLM_prompt = query_generate_interview_question(
        seen_problems=seen_problems,
        initial_prompt=CODING_INTERVIEW_PROMPT_V1,
        user_information=user_info,
        user_request=parsed_user_request,
    )

    print(LLM_prompt)


if __name__ == "__main__":
    generate_question()
