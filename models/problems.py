from datetime import datetime
from typing import List
import os


class SeenProblems:
    problem: str
    date_seen: datetime

    def __init__(self, problem: str, date_seen: datetime) -> None:
        self.problem = problem
        self.date_seen = date_seen


def load_seen_problems(directory: str) -> list[SeenProblems]:
    """Loads problems from a directory of files.
    NOTE: This does not load subdirectories, only files in the top level directory.
    """
    loaded_files: List[SeenProblems] = []
    # Generate a list of files, from an iterator checking to see if it's a file.
    files = [os.path.join(directory, f) for f in os.listdir(directory)]
    files = list(filter(os.path.isfile, files))
    # Sort the files by the modification time.
    files.sort(key=lambda x: os.path.getmtime(x))

    for file in files:
        # Get the last modified time of the file, as the date seen.
        problem_datetime = datetime.utcfromtimestamp(os.path.getmtime(file))
        with open(file) as f:
            loaded_files.append(
                SeenProblems(problem=f.read(), date_seen=problem_datetime)
            )
    return loaded_files
