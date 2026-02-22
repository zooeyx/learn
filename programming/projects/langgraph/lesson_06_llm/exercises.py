"""Lesson 6 Exercises: LLM Integration

Add LLM-powered classification to a pipeline. Run tests with:
    uv run pytest tests/test_lesson_06.py -v
"""
import os
from typing import Any, TypedDict

from pydantic import BaseModel, Field

from langgraph.graph import StateGraph, START, END


# --- Exercise 1: Define a Pydantic model for structured output ---

class SentimentOutput(BaseModel):
    """Structured output for sentiment analysis.
    
    Fields:
    - sentiment: str — "positive", "negative", or "neutral"
    - score: float — sentiment score from -1.0 (very negative) to 1.0 (very positive)
    - key_phrase: str — the phrase that most influenced the sentiment
    """
    # TODO: Define fields with Field descriptions
    ...


# --- Exercise 2: Create a mock LLM ---

class _MockResult:
    """Plain object with .model_dump(). Use instead of Pydantic models in mocks
    to avoid serialization warnings when LangGraph checkpoints the graph."""
    def __init__(self, **kwargs: Any):
        self.__dict__.update(kwargs)

    def model_dump(self) -> dict[str, Any]:
        return dict(self.__dict__)


class MockSentimentLLM:
    """Mock LLM that returns a result with .model_dump() based on keywords.

    Rules:
    - "love", "great", "amazing" → positive, score=0.9, key_phrase="positive keyword"
    - "hate", "terrible", "awful" → negative, score=-0.8, key_phrase="negative keyword"
    - Otherwise → neutral, score=0.0, key_phrase="no strong sentiment"

    Return _MockResult(...) — it has .model_dump() just like a Pydantic model.
    """
    def invoke(self, messages):
        # TODO: Implement mock logic
        # Extract content from last message, check keywords, return _MockResult(...)
        ...


# --- Exercise 3: Pipeline state ---

class FeedbackState(TypedDict, total=False):
    text: str
    sentiment: str
    score: float
    key_phrase: str
    response: str


# --- Exercise 4: Nodes ---

def get_sentiment_llm():
    """Get sentiment LLM — real or mock."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        return llm.with_structured_output(SentimentOutput)
    else:
        return MockSentimentLLM()


def analyze_sentiment(state: FeedbackState) -> dict[str, Any]:
    """Analyze sentiment using LLM.
    
    Steps:
    1. Get text from state
    2. Get the LLM via get_sentiment_llm()
    3. Invoke with a HumanMessage asking to analyze the text
    4. Convert result to dict with .model_dump()
    5. Return the sentiment, score, and key_phrase fields
    """
    # TODO: Implement
    ...


def create_response(state: FeedbackState) -> dict[str, Any]:
    """Create a response based on sentiment analysis.
    
    Rules:
    - positive (score > 0.5) → "Thank you for the positive feedback!"
    - negative (score < -0.5) → "We're sorry to hear that. We'll improve."
    - neutral → "Thank you for your feedback."
    """
    # TODO: Implement
    ...


# --- Exercise 5: Build the graph ---

def build_graph():
    """Build: analyze_sentiment → create_response"""
    # TODO: Implement
    ...
