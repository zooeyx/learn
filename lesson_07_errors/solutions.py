"""Lesson 7 Solutions"""
import logging
from typing import Any, TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.types import RetryPolicy

logger = logging.getLogger(__name__)


class AnalysisState(TypedDict, total=False):
    text: str
    word_count: int
    category: str
    confidence: float
    is_approved: bool
    block_reason: str
    summary: str


def analyze_text(state: AnalysisState) -> dict[str, Any]:
    try:
        text = state.get("text") or ""
        if not text:
            raise ValueError("Empty text")
        words = text.split()
        word_count = len(words)
        if word_count > 20:
            return {"word_count": word_count, "category": "long", "confidence": 0.9}
        elif word_count > 5:
            return {"word_count": word_count, "category": "medium", "confidence": 0.8}
        else:
            return {"word_count": word_count, "category": "short", "confidence": 0.7}
    except Exception as e:
        logger.warning("analyze_text.failed error=%s", str(e))
        return {"word_count": 0, "category": "unknown", "confidence": 0.0}


def approval_gate(state: AnalysisState) -> dict[str, Any]:
    try:
        confidence = state.get("confidence") or 0.0
        if confidence >= 0.75:
            return {"is_approved": True, "block_reason": ""}
        else:
            return {"is_approved": False, "block_reason": f"Low confidence: {confidence}"}
    except Exception as e:
        logger.warning("approval_gate.failed error=%s", str(e))
        return {"is_approved": False, "block_reason": f"Gate error: {str(e)}"}


def route_after_gate(state: AnalysisState) -> str:
    if state.get("is_approved"):
        return "summarize"
    return END


def summarize(state: AnalysisState) -> dict[str, Any]:
    category = state.get("category") or "unknown"
    word_count = state.get("word_count") or 0
    confidence = state.get("confidence") or 0.0
    return {"summary": f"Analysis: {category} text ({word_count} words, {confidence:.0%} confidence)"}


def build_graph():
    graph = StateGraph(AnalysisState)
    graph.add_node(
        "analyze_text",
        analyze_text,
        retry_policy=RetryPolicy(max_attempts=3, backoff_factor=2.0),
    )
    graph.add_node("approval_gate", approval_gate)
    graph.add_node("summarize", summarize)
    graph.add_edge(START, "analyze_text")
    graph.add_edge("analyze_text", "approval_gate")
    graph.add_conditional_edges(
        "approval_gate",
        route_after_gate,
        {"summarize": "summarize", END: END},
    )
    graph.add_edge("summarize", END)
    return graph.compile()
