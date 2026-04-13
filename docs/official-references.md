# Official References

These are the official references that are most useful for implementing the assignment.

## LangChain

- ChatOpenAI integration: https://docs.langchain.com/oss/python/integrations/chat/openai
- Agents overview (`create_agent`): https://docs.langchain.com/oss/python/langchain/agents
- Tools: https://docs.langchain.com/oss/python/langchain/tools
- `MessagesPlaceholder` API: https://api.python.langchain.com/en/latest/prompts/langchain_core.prompts.chat.MessagesPlaceholder.html
- `PydanticOutputParser` API: https://api.python.langchain.com/en/latest/core/output_parsers/langchain_core.output_parsers.pydantic.PydanticOutputParser.html
- `RecursiveCharacterTextSplitter` API: https://api.python.langchain.com/en/latest/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html
- Chroma vector store integration: https://docs.langchain.com/oss/python/integrations/vectorstores/chroma
- Chroma provider page: https://docs.langchain.com/oss/python/integrations/providers/chroma

## OpenAI

- OpenAI Platform docs: https://platform.openai.com/docs/overview

## Hugging Face Datasets

- `neural-bridge/rag-dataset-12000`: https://huggingface.co/datasets/neural-bridge/rag-dataset-12000
- Datasets loading guide: https://huggingface.co/docs/datasets/loading

## Chroma

- Chroma CLI install: https://docs.trychroma.com/cli/install

## Notes

- For Step 2, `ChatPromptTemplate + MessagesPlaceholder` is recommended over the legacy `ConversationChain` pattern because it matches modern LangChain usage more closely.
- Step 4 uses the `context/question/answer` structure from `neural-bridge/rag-dataset-12000`.
- Step 4 requires a base non-vector implementation, and a Chroma-based vector search version is recommended as bonus work.
