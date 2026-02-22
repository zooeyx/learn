"""Lesson 5 Solutions"""
import operator
from typing import Annotated, Any, TypedDict

from langgraph.graph import StateGraph, START, END


class ResearchState(TypedDict, total=False):
    query: str
    sources: Annotated[list[dict], operator.add]
    keywords: Annotated[list[str], operator.add]
    relevance_score: float


def extract_keywords(state: ResearchState) -> dict[str, Any]:
    query = state.get("query") or ""
    words = [w.lower() for w in query.split() if len(w) > 3]
    return {"keywords": words}


def search_web(state: ResearchState) -> dict[str, Any]:
    query = state.get("query") or ""
    return {
        "sources": [{"source": "web", "title": f"Web result for: {query}"}],
        "relevance_score": 0.7,
    }


def search_docs(state: ResearchState) -> dict[str, Any]:
    query = state.get("query") or ""
    return {
        "sources": [{"source": "docs", "title": f"Doc result for: {query}"}],
        "relevance_score": 0.9,
    }


def min_reducer(current: float, new: float) -> float:
    return min(current, new)


def build_pipeline():
    graph = StateGraph(ResearchState)
    graph.add_node("extract_keywords", extract_keywords)
    graph.add_node("search_web", search_web)
    graph.add_node("search_docs", search_docs)
    graph.add_edge(START, "extract_keywords")
    graph.add_edge("extract_keywords", "search_web")
    graph.add_edge("search_web", "search_docs")
    graph.add_edge("search_docs", END)
    return graph.compile()
