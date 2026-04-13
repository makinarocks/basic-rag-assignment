"""Step 2: A chatbot with memory.

Goal
- Make earlier conversation turns affect later responses.
- Use `MessagesPlaceholder` in a modern LangChain style.

Suggested scenario
1. "My name is Jimin."
2. "I am a backend engineering intern."
3. "Tell me my name and role again."
"""

from __future__ import annotations

from typing import Any

WINDOW_SIZE = 6


def build_chat_chain(window_size: int = WINDOW_SIZE):
    """TODO: Build a chain that includes MessagesPlaceholder."""
    raise NotImplementedError("Implement Step 2 build_chat_chain.")


def trim_history(history: list[tuple[str, str]], window_size: int = WINDOW_SIZE) -> list[tuple[str, str]]:
    """TODO: Trim the history if you only want to keep recent messages."""
    raise NotImplementedError("Implement Step 2 trim_history.")


def run_turn(chain: Any, history: list[tuple[str, str]], user_input: str) -> tuple[str, list[tuple[str, str]]]:
    """TODO: Execute one turn and return the updated history."""
    raise NotImplementedError("Implement Step 2 run_turn.")


def demo_conversation() -> None:
    """TODO: Run and inspect at least three turns of example conversation."""
    raise NotImplementedError("Implement Step 2 demo_conversation.")


def main() -> None:
    demo_conversation()


if __name__ == "__main__":
    main()
