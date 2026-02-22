"""Lesson 6 Solutions"""
import os
from typing import Any, TypedDict

from pydantic import BaseModel, Field

from langgraph.graph import StateGraph, START, END


class SentimentOutput(BaseModel):
    sentiment: str = Field(description="Sentiment: positive, negative, or neutral")
    score: float = Field(description="Score from -1.0 to 1.0")
    key_phrase: str = Field(description="Most influential phrase")


class _MockResult:
    """Plain object with .model_dump() — avoids Pydantic serialization warnings."""
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def model_dump(self) -> dict[str, Any]:
        return dict(self.__dict__)


class MockSentimentLLM:
    def invoke(self, messages):
        content = messages[-1].content if hasattr(messages[-1], 'content') else str(messages[-1])
        content_lower = content.lower()
        if any(w in content_lower for w in ["love", "great", "amazing"]):
            return _MockResult(sentiment="positive", score=0.9, key_phrase="positive keyword")
        elif any(w in content_lower for w in ["hate", "terrible", "awful"]):
            return _MockResult(sentiment="negative", score=-0.8, key_phrase="negative keyword")
        else:
            return _MockResult(sentiment="neutral", score=0.0, key_phrase="no strong sentiment")


class FeedbackState(TypedDict, total=False):
    text: str
    sentiment: str
    score: float
    key_phrase: str
    response: str


def get_sentiment_llm():
    api_key = os.environ.get("OPENAI_API_KEY")
    if api_key:
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        return llm.with_structured_output(SentimentOutput)
    else:
        return MockSentimentLLM()


def analyze_sentiment(state: FeedbackState) -> dict[str, Any]:
    text = state.get("text") or ""
    llm = get_sentiment_llm()
    from langchain_core.messages import HumanMessage
    result = llm.invoke([HumanMessage(content=f"Analyze the sentiment of: {text}")])
    output = result.model_dump()
    return {
        "sentiment": output["sentiment"],
        "score": output["score"],
        "key_phrase": output["key_phrase"],
    }


def create_response(state: FeedbackState) -> dict[str, Any]:
    score = state.get("score") or 0.0
    if score > 0.5:
        return {"response": "Thank you for the positive feedback!"}
    elif score < -0.5:
        return {"response": "We're sorry to hear that. We'll improve."}
    else:
        return {"response": "Thank you for your feedback."}


def build_graph():
    graph = StateGraph(FeedbackState)
    graph.add_node("analyze_sentiment", analyze_sentiment)
    graph.add_node("create_response", create_response)
    graph.add_edge(START, "analyze_sentiment")
    graph.add_edge("analyze_sentiment", "create_response")
    graph.add_edge("create_response", END)
    return graph.compile()
