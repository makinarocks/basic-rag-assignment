"""Step 3: Structured output.

Goal
- Produce a validated structured result instead of free-form text.
- Define a Pydantic model with `intent`, `priority`, and `answer`.
- Consider parse failure cases.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class ClassifiedResponse(BaseModel):
    """Schema for the LLM response."""

    intent: str = Field(description="One of: question, greeting, request")
    priority: int = Field(ge=1, le=5, description="1 is low priority, 5 is very high priority")
    answer: str = Field(description="The final answer shown to the user")


def build_parser():
    """TODO: Create a PydanticOutputParser."""
    raise NotImplementedError("Implement Step 3 build_parser.")


def build_prompt(parser) -> str:
    """TODO: Write a prompt that includes the parser format instructions."""
    raise NotImplementedError("Implement Step 3 build_prompt.")


def classify_message(user_input: str) -> ClassifiedResponse:
    """TODO: Convert user input into the structured schema."""
    raise NotImplementedError("Implement Step 3 classify_message.")


def main() -> None:
    """TODO: Complete the Step 3 demo."""
    raise NotImplementedError("Implement Step 3 main.")


if __name__ == "__main__":
    main()
