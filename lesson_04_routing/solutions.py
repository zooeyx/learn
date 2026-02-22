"""Lesson 4 Solutions"""
from typing import Any, TypedDict

from langgraph.graph import StateGraph, START, END


class ReviewState(TypedDict, total=False):
    text: str
    language: str
    sentiment: str
    response: str
    status: str
    force_continue: bool


def route_after_detect(state: ReviewState) -> str:
    if state.get("force_continue"):
        return "analyze"
    language = state.get("language") or "unknown"
    if language == "unknown":
        return END
    elif language == "en":
        return "analyze"
    else:
        return "translate"


def detect_language(state: ReviewState) -> dict[str, Any]:
    text = (state.get("text") or "").lower()
    if "bonjour" in text or "merci" in text:
        return {"language": "fr"}
    elif "hola" in text or "gracias" in text:
        return {"language": "es"}
    elif text.isascii():
        return {"language": "en"}
    else:
        return {"language": "unknown"}


def translate(state: ReviewState) -> dict[str, Any]:
    text = state.get("text") or ""
    return {"text": f"[translated] {text}"}


def analyze(state: ReviewState) -> dict[str, Any]:
    text = (state.get("text") or "").lower()
    if any(w in text for w in ["great", "love", "excellent"]):
        return {"sentiment": "positive"}
    elif any(w in text for w in ["bad", "hate", "terrible"]):
        return {"sentiment": "negative"}
    else:
        return {"sentiment": "neutral"}


def create_response(state: ReviewState) -> dict[str, Any]:
    sentiment = state.get("sentiment") or "neutral"
    if sentiment == "positive":
        return {"response": "Thank you for your kind words!", "status": "resolved"}
    elif sentiment == "negative":
        return {"response": "We're sorry. We'll improve.", "status": "needs_followup"}
    else:
        return {"response": "Thank you for your feedback.", "status": "resolved"}


def build_graph():
    graph = StateGraph(ReviewState)
    graph.add_node("detect_language", detect_language)
    graph.add_node("translate", translate)
    graph.add_node("analyze", analyze)
    graph.add_node("create_response", create_response)
    
    graph.add_edge(START, "detect_language")
    graph.add_conditional_edges(
        "detect_language",
        route_after_detect,
        {
            END: END,
            "analyze": "analyze",
            "translate": "translate",
        },
    )
    graph.add_edge("translate", "analyze")
    graph.add_edge("analyze", "create_response")
    graph.add_edge("create_response", END)
    
    return graph.compile()
