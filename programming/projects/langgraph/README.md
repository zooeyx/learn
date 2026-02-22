# Learn LangGraph: Progressive Pipeline Course

A hands-on course that teaches you to build AI pipelines with LangGraph, from Python fundamentals to a complete support-ticket pipeline.

## Setup

```bash
cd ~/learn
uv sync
```

## Lessons

| # | Topic | Key Concepts | LLM Required? |
|---|-------|-------------|---------------|
| 1 | Python Foundations | TypedDict, Annotated, async/await | No |
| 2 | Your First Graph | StateGraph, nodes, edges, compile, invoke | No |
| 3 | Multi-Node Pipeline | Linear chains, partial state updates | No |
| 4 | Conditional Routing | Conditional edges, early exits, routing functions | No |
| 5 | Reducers | operator.add, custom reducers, state accumulation | No |
| 6 | LLM Integration | ChatOpenAI, structured output, Pydantic at boundary | Yes (mock fallback) |
| 7 | Error Handling | try/except fallback, RetryPolicy, fail-closed gates | Yes (mock fallback) |
| 8 | Parallel Execution | Fan-out / fan-in, parallel nodes, reducer merging | No |
| 9 | Checkpointing | MemorySaver, thread_id, interrupt, resume | No |
| 10 | Capstone | 6-node support pipeline combining everything | Yes (mock fallback) |

## How to Use

Each lesson has three files:
- **concepts.py** — Working examples with inline comments (run to see output)
- **exercises.py** — TODO stubs for you to complete
- **solutions.py** — Completed versions (peek only when stuck)

## Running

```bash
# Run a concept file to see it in action
uv run python lesson_02_first_graph/concepts.py

# Run tests to verify your exercises
uv run pytest tests/test_lesson_02.py -v

# Run all tests
uv run pytest tests/ -v

# Run the capstone
uv run python lesson_10_capstone/pipeline.py
```

## Environment

For lessons 6+ (LLM integration), set your OpenAI API key:
```bash
export OPENAI_API_KEY=sk-...
```
All LLM lessons include a mock fallback so you can work offline.
