# Reviewer Rubric

## Quick Demo Prompts

### Step 1
- `Introduce yourself in one sentence.`
- `What is the first concept a beginner should learn in LangChain?`

### Step 2
- `My name is Jimin.`
- `I am a backend engineering intern.`
- `Tell me my name and role again.`

### Step 3
- `Hello!`
- `My laptop is broken. Tell me the replacement process.`
- `Classify this urgent customer request for me.`

### Step 4
- Demo 3 questions from the dataset `test` split
- Print part of the retrieved context used for answering
- Compare the predicted answer with the dataset answer side by side

### Step 5
- One question chosen from the dataset
- `I am really nervous today. Please encourage me.`

## Step-by-Step Checklist

### Step 1
- [ ] Reads model settings from `.env`
- [ ] Reads the input file and creates an output file
- [ ] Handles empty files or empty lines safely

### Step 2
- [ ] Earlier conversation affects later responses
- [ ] The author can explain the history structure
- [ ] If message count is limited, the reason is documented or explainable

### Step 3
- [ ] Produces a consistent JSON/Pydantic structure
- [ ] Validates the `priority` range
- [ ] Handles parsing failures

### Step 4
- [ ] Loads the Hugging Face dataset successfully
- [ ] Uses `train` contexts as the retrieval corpus
- [ ] Runs retrieval + answer generation on `test` questions
- [ ] Prints logs or outputs that compare predictions with dataset answers
- [ ] If the bonus is implemented, Chroma retrieval actually works
- [ ] If both modes exist, the author can explain the difference between basic and Chroma retrieval

### Step 5
- [ ] Uses the tool when external knowledge retrieval is needed
- [ ] Avoids unnecessary tool calls during normal conversation
- [ ] Reuses Step 4 assets cleanly

## Common Bonus Points

- The run instructions are clearly documented in the README
- The function boundaries and file structure are simple and readable
- The reflection notes describe real trial-and-error and lessons learned
