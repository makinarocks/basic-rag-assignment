# LangChain-Step-By-Step

This repository is a step-by-step onboarding assignment for learning how to build LLM applications with LangChain and OpenAI.
Interns should implement `step_1.py` through `step_5.py` in order and finish with a small AI assistant that can handle both **external RAG dataset lookup and general conversation**.

> This assignment assumes **Python 3.11+** or higher, **LangChain v1**, and an **OpenAI API key**.
> For Step 2, the assignment uses the more modern `ChatPromptTemplate + MessagesPlaceholder` pattern instead of the older `ConversationChain` style.

## Learning Goals

- Safely manage `.env` files and API keys
- Run basic LLM calls with [`ChatOpenAI`](https://reference.langchain.com/python/langchain-openai/chat_models/base/ChatOpenAI)
- Feed conversation history back into prompts
- Build a simple RAG workflow using a Hugging Face dataset
- Structure LLM outputs with Pydantic
- Let an agent decide when to use a tool

## Repository Structure

```text
.
├── data/
│   └── questions.txt
├── docs/
│   └── reviewer-rubric.md
├── outputs/
│   └── .gitkeep
├── .env.example
├── requirements.txt
├── step_1.py
├── step_2.py
├── step_3.py
├── step_4.py
├── step_5.py
└── step_6.py
```

## Getting Started

1. Fork or clone this repository.
2. Create a virtual environment (you can set up your development environment in any way you prefer). Make sure to use Python 3.11 or higher.
   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```
   To deactivate the virtual environment later, run:
   ```bash
   deactivate
   ```
3. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and fill in `OPENAI_API_KEY`.
   ```bash
   cp .env.example .env
   ```
5. Implement the assignment in order, starting from `step_1.py`.

## Assignment Rules

- Each step should **extend the result of the previous step**.
- If you get stuck, read the official docs first.
- Open a Pull Request after completing Step 6.

## Step Overview

| Step | Topic | Goal | What to Check |
| --- | --- | --- | --- |
| 1 | Basic Setup | Read `questions.txt`, generate answers, and save them to `outputs/step_1_output.txt` | API integration, file I/O |
| 2 | Conversation Memory | Build a chatbot that remembers earlier turns | Name/context retention |
| 3 | Structured Output | Return `intent` and `answer` as JSON/Pydantic | Output parsing, validation |
| 4 | Simple RAG | Build dataset-based QA with `neural-bridge/rag-dataset-12000` | Dataset loading, Vector DB insertion, context retrieval, answer generation |
| 5 | Final Agent | Build an assistant that connects with the Vector DB to answer dataset questions | Tools, agent flow, reuse |
| 6 | Language Filter | Detect language and refuse to answer if not Japanese or English | Guardrails, prompt engineering or routing |

---

## Step 1 — First Conversation with an LLM

**Mission**
- Read `data/questions.txt` line by line.
- Send each question to `ChatOpenAI`.
- Save the questions and answers in a readable format to `outputs/step_1_output.txt`.

**Required**
- Read the API key from `.env`
- Ignore empty lines
- Overwrite the output file on each run

---

## Step 2 — A Chatbot with Memory

**Mission**
- Build a chatbot that can continue a multi-turn conversation.
- The following flow should work:
  - `My name is Jimin.`
  - `What is my name?`

**Required**
- Use `MessagesPlaceholder`
- Choose either full-history memory or a recent-window memory approach
- Manually verify at least 3 turns of conversation

**Hint**
- In modern LangChain flows, `ChatPromptTemplate + MessagesPlaceholder` is more instructive than the legacy `ConversationChain` pattern.
- Managing `history` as a list is perfectly fine for this assignment.


---

## Step 3 — Structured Output

**Mission**
- Analyze user input and return it in the following format.

```json
{
  "intent": "question | greeting | request",
  "answer": "..."
}
```

**Required**
- Use `PydanticOutputParser` or an equivalent explicit schema validation flow
- Handle parse failures with retries or explicit error handling


---

## Step 4 — External Data with Simple RAG

**Mission**
- Use the Hugging Face dataset [`neural-bridge/rag-dataset-12000`](https://huggingface.co/datasets/neural-bridge/rag-dataset-12000) to build a simple RAG pipeline.
- Use the dataset's `context`, `question`, and `answer` fields to implement a retrieval + answer generation flow.
- At minimum, run retrieval-based answering on a few `test` questions and compare your output with the provided answers.

**Required**
- Load `neural-bridge/rag-dataset-12000` with the `datasets` library
- Use the `train` split `context` field as the retrieval corpus
- Pick a few `test` split questions and run retrieval + generation on them
- Only place relevant context or chunks into the prompt

**Vector DB Implementation (Required)**
- A Vector DB (e.g., Chroma) is required for retrieval.
- Extract the `context` from exactly `train[:200]` and convert them into `Document` objects.
- Create embeddings and store them in a Vector DB collection.
- If the retrieved context is not enough to answer, say that the answer could not be verified from the context.

**Suggested Implementation Order**
1. Load the dataset with `load_dataset()`
2. Slice the dataset to `train[:200]` and `test[:20]`
3. Convert `train[:200]` contexts into `Document` objects and store them in a Vector DB via embeddings
4. Retrieve relevant context using similarity search for each `test` question
5. Insert the retrieved context into the prompt and generate an answer
6. Compare your result with the dataset `answer` or log the differences



**Short Chroma Guide**
- Install these packages in your local Python environment:
  ```bash
  pip install langchain-chroma chromadb
  ```
- Use `persist_directory` if you want a local persistent DB.
- If you want to try a local server flow, install the Chroma CLI and run `chroma run`.
- For installation details and the latest setup instructions, refer to the official Chroma website and docs:
  - https://www.trychroma.com/
  - https://docs.trychroma.com/

---

## Step 5 — Autonomous Assistant

**Mission**
- Integrate with the Vector DB from Step 4.
- If a user question needs external knowledge retrieval, use the Vector DB lookup tool.
- If it is general conversation, let the LLM answer directly.
- In other words, let the LLM decide whether it should use the retrieval tool.

**Required**
- Define at least one tool
- Make the agent's reasoning or execution log inspectable
- Demo both of the following:
  - one question selected from the dataset
  - one general conversation prompt

---

## Step 6 — Language Routing / Filtering

**Mission**
- Add a guardrail that detects the language of the user's input before answering.
- If the question is **not** in Japanese (**日本語**) or English (**English**), the assistant must decline to answer (e.g., "I can only answer in Japanese or English.").
- This rule applies to both general conversation and dataset questions.

**Required**
- Use LangChain routing mechanisms or direct prompt engineering to filter based on language.
- Demo an allowed language query and a blocked language query (e.g., Korean, Spanish).


---

## Submission Guide

- **Open a Pull Request** to track and submit your progress.
- In your PR description, briefly include what you implemented in each step.
- **AI Coding Tools:** You are completely free to use AI coding tools (such as Antigravity, Claude Code, etc.) for this assignment. If you need a license or support for any specific AI coding tool, please let us know and we will provide it for you.

