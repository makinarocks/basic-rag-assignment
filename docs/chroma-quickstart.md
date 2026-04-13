# Chroma Quickstart

This is a short guide for the **optional bonus implementation** in Step 4. It assumes you will put the `train` split contexts from `neural-bridge/rag-dataset-12000` into Chroma.

## 1) Install

Based on the LangChain Python docs, you need `langchain-chroma` for the Chroma integration.

```bash
pip install langchain-chroma chromadb
```

- `langchain-chroma`: the LangChain integration package for Chroma vector stores
- `chromadb`: local Chroma runtime and CLI

## 2) Easiest Approach: Local Persistent DB

The simplest setup is to store everything in a local folder without running a separate server.

```python
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = Chroma(
    collection_name="rag_dataset_12000",
    embedding_function=embeddings,
    persist_directory="./chroma_db",
)
```

## 3) Example Flow

```python
train_rows, eval_rows = load_rag_dataset()
documents = build_corpus_documents(train_rows)
vector_store.add_documents(documents)
results = vector_store.similarity_search(eval_rows[0]["question"], k=3)
```

Then:
- put the retrieved context into the prompt
- generate an answer
- compare it with the dataset answer

## 4) If You Want a Local Server

If you want to try the CLI/server approach, you can run:

```bash
chroma run
```

Then connect from LangChain using a localhost-based client configuration.

## 5) Does It Work on Windows?

Yes. For this assignment, the recommended option is the **local persistent DB** approach, which is usually simpler to try on Windows because it has fewer system-level dependencies.

## 6) Recommended Scope for This Assignment

- Required: base non-vector retrieval implementation
- Bonus: Chroma-based semantic search
- Reflection: compare retrieval quality, implementation difficulty, and how your outputs differ from the dataset answers

## Reference Links

- LangChain Chroma integration: https://docs.langchain.com/oss/python/integrations/vectorstores/chroma
- LangChain Chroma provider page: https://docs.langchain.com/oss/python/integrations/providers/chroma
- Chroma CLI install: https://docs.trychroma.com/cli/install
