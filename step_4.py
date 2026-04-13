"""Step 4: External data with Simple RAG.

Goal
- Load the Hugging Face dataset `neural-bridge/rag-dataset-12000`.
- Use the `train` split contexts as the retrieval corpus.
- Find relevant context for `test` split questions and answer them.

Notes
- The base assignment can start without a vector database.
- Simple methods like keyword overlap or string matching are acceptable for context selection.
- A Chroma-based vector search version can be added as bonus work.
"""

from __future__ import annotations

from typing import Any

DATASET_NAME = "neural-bridge/rag-dataset-12000"
TRAIN_SPLIT = "train[:200]"
EVAL_SPLIT = "test[:20]"


def load_rag_dataset(train_split: str = TRAIN_SPLIT, eval_split: str = EVAL_SPLIT):
    """TODO: Load the train/eval splits with datasets.load_dataset."""
    raise NotImplementedError("Implement Step 4 load_rag_dataset.")


def build_corpus_documents(rows: list[dict[str, Any]]):
    """TODO: Convert train rows into Documents or an equivalent search structure."""
    raise NotImplementedError("Implement Step 4 build_corpus_documents.")


def select_relevant_contexts(question: str, contexts: list[Any], top_k: int = 3) -> list[Any]:
    """TODO: Select the top-k most relevant contexts for a question."""
    raise NotImplementedError("Implement Step 4 select_relevant_contexts.")


def answer_with_context(question: str, relevant_contexts: list[Any]) -> str:
    """TODO: Put the selected context into the prompt and answer the question."""
    raise NotImplementedError("Implement Step 4 answer_with_context.")


def evaluate_sample_predictions(eval_rows: list[dict[str, Any]]) -> None:
    """TODO: Print a few predicted answers next to the dataset answers."""
    raise NotImplementedError("Implement Step 4 evaluate_sample_predictions.")


def main() -> None:
    """TODO: Complete the Step 4 demo."""
    raise NotImplementedError("Implement Step 4 main.")


if __name__ == "__main__":
    main()
