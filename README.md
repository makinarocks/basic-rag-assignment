# LangChain-Step-By-Step

This repository is a step-by-step onboarding assignment for learning how to build LLM applications with LangChain and OpenAI.
Interns should implement `step_1.py` through `step_5.py` in order and finish with a small AI assistant that can handle both **external RAG dataset lookup and general conversation**.

> This assignment assumes **Python 3.11+**, **LangChain v1**, and an **OpenAI API key**.
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
│   ├── official-references.md
│   └── reviewer-rubric.md
├── outputs/
│   └── .gitkeep
├── .env.example
├── requirements.txt
├── step_1.py
├── step_2.py
├── step_3.py
├── step_4.py
└── step_5.py
```

## Getting Started

1. Fork or clone this repository.
2. Create a virtual environment.
   ```bash
   python -m venv .venv
   source .venv/bin/activate
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
- Run each step yourself and leave a short note in the **reflection section** at the bottom of `README.md`.
- If you get stuck, read the official docs first, and mention which docs helped you in your reflection.
- Open a Pull Request after completing Step 5.

## Step Overview

| Step | Topic | Goal | What to Check |
| --- | --- | --- | --- |
| 1 | Basic Setup | Read `questions.txt`, generate answers, and save them to `outputs/step_1_output.txt` | API integration, file I/O |
| 2 | Conversation Memory | Build a chatbot that remembers earlier turns | Name/context retention |
| 3 | Structured Output | Return `intent`, `priority`, and `answer` as JSON/Pydantic | Output parsing, validation |
| 4 | Simple RAG | Build dataset-based QA with `neural-bridge/rag-dataset-12000` | Dataset loading, context retrieval, answer generation, optional Chroma bonus |
| 5 | Final Agent | Build an assistant that decides when dataset lookup is needed | Tools, agent flow, reuse |

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

**Suggested Function Split**
- `load_questions()`
- `build_llm()`
- `answer_questions()`
- `save_answers()`

**Run Example**
```bash
python step_1.py
```

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

**Run Example**
```bash
python step_2.py
```

---

## Step 3 — Structured Output

**Mission**
- Analyze user input and return it in the following format.

```json
{
  "intent": "question | greeting | request",
  "priority": 1,
  "answer": "..."
}
```

**Required**
- Use `PydanticOutputParser` or an equivalent explicit schema validation flow
- Restrict `priority` to the range 1 to 5
- Handle parse failures with retries or explicit error handling

**Run Example**
```bash
python step_3.py
```

---

## Step 4 — External Data with Simple RAG

**Mission**
- Use the Hugging Face dataset `neural-bridge/rag-dataset-12000` to build a simple RAG pipeline.
- Use the dataset's `context`, `question`, and `answer` fields to implement a retrieval + answer generation flow.
- At minimum, run retrieval-based answering on a few `test` questions and compare your output with the provided answers.

**Required**
- Load `neural-bridge/rag-dataset-12000` with the `datasets` library
- Use the `train` split `context` field as the retrieval corpus
- Pick a few `test` split questions and run retrieval + generation on them
- Only place relevant context or chunks into the prompt

**Base Implementation (Required)**
- You may implement this step without a vector database.
- For example, keyword matching, simple scoring, or rule-based top-k retrieval is acceptable.
- Because the dataset is large, it is fine to start with a small subset like `train[:200]` and `test[:20]`.
- If the retrieved context is not enough to answer, say that the answer could not be verified from the context.

**Bonus Implementation (Optional)**
- Add a Chroma-based vector search version for bonus credit.
- Suggested flow:
  1. Convert `train` split `context` entries into `Document` objects
  2. Create embeddings with `OpenAIEmbeddings`
  3. Store them in a Chroma collection
  4. Retrieve relevant context with `similarity_search` or a retriever
  5. Generate the answer using the retrieved results
- If you implement both the base and Chroma versions, state in the README which one is the default.

**Suggested Implementation Order**
1. Load the dataset with `load_dataset()`
2. Slice the `train` and `test` subsets
3. Prepare the `train` contexts as searchable units
4. Retrieve relevant context for each `test` question
5. Insert the retrieved context into the prompt and generate an answer
6. Compare your result with the dataset `answer` or log the differences

**Optional CLI Ideas**
- `--mode basic` for non-vector retrieval
- `--mode chroma` for Chroma-based retrieval
- `--split train[:200] --eval-split test[:20]` to control subset sizes
- Briefly compare the two modes in your README reflection

**Run Example**
```bash
python step_4.py
```

**Short Chroma Guide**
- Optionally install these packages in your local Python environment:
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
- If a user question needs external knowledge retrieval, use the Step 4 dataset lookup tool.
- If it is general conversation, let the LLM answer directly.
- In other words, let the LLM decide whether it should use a tool.

**Required**
- Define at least one tool
- Make the agent's reasoning or execution log inspectable
- Demo both of the following:
  - one question selected from the dataset
  - one general conversation prompt

**Run Example**
```bash
python step_5.py
```

---

## Submission Guide

Include the following in your Pull Request.

- What you implemented in each step
- What blocked you and how you resolved it
- Which dataset split/subset you used in Steps 4 and 5
- Which Step 5 demo questions you used
- One or two things you would improve next

## Evaluation Criteria

- **Correctness:** Did you satisfy the requirements?
- **Understanding:** Can you explain why you chose this structure?
- **Code quality:** Are function boundaries, naming, comments, and exception handling reasonable?
- **Extensibility:** Do Steps 3–5 evolve naturally rather than feeling forced?

## Reflection Template

Copy the template below and paste it at the bottom of the README.

```md
## Step 1 Reflection
- What I implemented:
- What was difficult:
- Docs I used:

## Step 2 Reflection
- What I implemented:
- What was difficult:
- Docs I used:
```
