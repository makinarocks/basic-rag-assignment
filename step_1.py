"""Step 1: First conversation with an LLM.

TODO
1. Load `.env`.
2. Read `data/questions.txt` line by line.
3. Create a `ChatOpenAI` instance.
4. Save answers for each question to `outputs/step_1_output.txt`.

Recommended implementation points
- Remove empty lines
- Handle exceptions: missing API key, missing file
- Split functions: load / build / invoke / save
"""

from __future__ import annotations

from pathlib import Path

QUESTIONS_PATH = Path("data/questions.txt")
OUTPUT_PATH = Path("outputs/step_1_output.txt")


def load_questions(path: Path) -> list[str]:
    """TODO: Read the question file and return non-empty lines."""
    raise NotImplementedError("Implement Step 1 load_questions.")


def build_llm():
    """TODO: Create and return a ChatOpenAI instance."""
    raise NotImplementedError("Implement Step 1 build_llm.")


def answer_questions(llm, questions: list[str]) -> list[str]:
    """TODO: Generate an answer for each question."""
    raise NotImplementedError("Implement Step 1 answer_questions.")


def save_answers(path: Path, questions: list[str], answers: list[str]) -> None:
    """TODO: Save the questions and answers in a readable format."""
    raise NotImplementedError("Implement Step 1 save_answers.")


def main() -> None:
    """TODO: Complete the Step 1 execution flow."""
    raise NotImplementedError("Implement Step 1 main.")


if __name__ == "__main__":
    main()
