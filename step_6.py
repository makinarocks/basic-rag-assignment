"""Step 6: Language Routing / Filtering.

Goal
- Detect the language of the user's input.
- If the language is not Japanese or English, gracefully decline to answer.
- Combine this with the Autonomous Assistant from Step 5.

Suggested demo
- "한국어로 대답해줘." (Korean - should be rejected)
- "Tell me a joke." (English - should be allowed)
"""

from __future__ import annotations

from typing import Any


def check_language(user_input: str) -> bool:
    """TODO: Determine if the language is Japanese or English."""
    raise NotImplementedError("Implement Step 6 check_language.")


def build_filtered_agent() -> Any:
    """TODO: Build an agent that filters by language before proceeding."""
    raise NotImplementedError("Implement Step 6 build_filtered_agent.")


def run_demo(agent: Any) -> None:
    """TODO: Demo allowed and blocked language queries."""
    raise NotImplementedError("Implement Step 6 run_demo.")


def main() -> None:
    """TODO: Complete the Step 6 execution flow."""
    raise NotImplementedError("Implement Step 6 main.")


if __name__ == "__main__":
    main()
