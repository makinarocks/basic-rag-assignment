"""Step 5: Autonomous assistant.

Goal
- Use a tool when external knowledge retrieval is needed.
- Answer directly when the conversation does not need retrieval.
- Reuse the Step 4 assets.

Suggested demo
- One question taken from the dataset
- "I am feeling a bit down today. Please say something encouraging."
"""

from __future__ import annotations

from typing import Any


def build_dataset_lookup_tool():
    """TODO: Define a tool that reuses the Step 4 dataset retrieval logic."""
    raise NotImplementedError("Implement Step 5 build_dataset_lookup_tool.")


def build_agent() -> Any:
    """TODO: Build an agent with create_agent."""
    raise NotImplementedError("Implement Step 5 build_agent.")


def run_demo(agent: Any) -> None:
    """TODO: Demo one dataset question and one general conversation prompt."""
    raise NotImplementedError("Implement Step 5 run_demo.")


def main() -> None:
    """TODO: Complete the Step 5 execution flow."""
    raise NotImplementedError("Implement Step 5 main.")


if __name__ == "__main__":
    main()
