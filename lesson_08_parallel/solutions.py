"""Lesson 8 Solutions"""
import operator
from typing import Annotated, Any, TypedDict

from langgraph.graph import StateGraph, START, END


class ArticleState(TypedDict, total=False):
    text: str
    word_count: int
    keywords: Annotated[list[str], operator.add]
    findings: Annotated[list[str], operator.add]
    reading_level: str
    summary: str


def count_words(state: ArticleState) -> dict[str, Any]:
    text = state.get("text") or ""
    count = len(text.split())
    return {"word_count": count, "findings": [f"word_count:{count}"]}


def extract_keywords(state: ArticleState) -> dict[str, Any]:
    text = state.get("text") or ""
    words = list(set(w.lower() for w in text.split() if len(w) > 5))
    return {"keywords": words, "findings": [f"keywords:{len(words)}"]}


def assess_reading_level(state: ArticleState) -> dict[str, Any]:
    text = state.get("text") or ""
    words = text.split()
    if not words:
        return {"reading_level": "beginner", "findings": ["reading_level:beginner"]}
    avg_len = sum(len(w) for w in words) / len(words)
    if avg_len > 7:
        level = "advanced"
    elif avg_len > 5:
        level = "intermediate"
    else:
        level = "beginner"
    return {"reading_level": level, "findings": [f"reading_level:{level}"]}


def create_summary(state: ArticleState) -> dict[str, Any]:
    wc = state.get("word_count") or 0
    kw = state.get("keywords") or []
    rl = state.get("reading_level") or "unknown"
    return {"summary": f"{wc} words, {len(kw)} keywords, {rl} level"}


def build_graph():
    graph = StateGraph(ArticleState)
    graph.add_node("count_words", count_words)
    graph.add_node("extract_keywords", extract_keywords)
    graph.add_node("assess_reading_level", assess_reading_level)
    graph.add_node("create_summary", create_summary)
    
    graph.add_edge(START, "count_words")
    graph.add_edge(START, "extract_keywords")
    graph.add_edge(START, "assess_reading_level")
    
    graph.add_edge("count_words", "create_summary")
    graph.add_edge("extract_keywords", "create_summary")
    graph.add_edge("assess_reading_level", "create_summary")
    
    graph.add_edge("create_summary", END)
    return graph.compile()
