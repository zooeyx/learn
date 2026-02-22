"""Lesson 2 Solutions"""
from typing import Any, TypedDict

from langgraph.graph import StateGraph, START, END


class MessageState(TypedDict, total=False):
    text: str
    word_count: int
    is_long: bool


def count_words(state: MessageState) -> dict[str, Any]:
    text = state.get("text") or ""
    return {"word_count": len(text.split())}


def check_length(state: MessageState) -> dict[str, Any]:
    count = state.get("word_count") or 0
    return {"is_long": count > 10}


def build_graph():
    graph = StateGraph(MessageState)
    graph.add_node("count_words", count_words)
    graph.add_node("check_length", check_length)
    graph.add_edge(START, "count_words")
    graph.add_edge("count_words", "check_length")
    graph.add_edge("check_length", END)
    return graph.compile()
