from typing import List, Optional, Union

# Structure:
# A prompt should be a series of snippets.
# The default delimiter between snippets is a new line.


class Prompt:
    snippets: List[str]

    def __init__(self, starting_prompt: Optional[str] = None) -> None:
        if starting_prompt is not None:
            self.snippets: List[str] = [starting_prompt]
        else:
            self.snippets: List[str] = []

    def to_string(self, snippet_separator: str = "\n") -> str:
        return snippet_separator.join(self.snippets)

    def append(self, appending_object: Union["Prompt", str]) -> None:
        if isinstance(appending_object, Prompt):
            self.snippets.extend(appending_object)
        elif isinstance(appending_object, str):
            self.snippets.append(appending_object)
        else:
            raise TypeError(" Only strings or Prompts can be appended to a prompt")

    def __add__(self, other: Union["Prompt", str]) -> "Prompt":
        new_prompt = Prompt()
        # We append both ourself, and the other object, this way we can preserve both list of snippets.
        new_prompt.append(self)
        new_prompt.append(other)
        return new_prompt

    def __getitem__(self, index) -> str:
        return self.snippets[index]

    def __len__(self) -> int:
        length = 0
        for s in self.snippets:
            length += len(s)
        return length

    def __str__(self) -> str:
        return self.to_string()
