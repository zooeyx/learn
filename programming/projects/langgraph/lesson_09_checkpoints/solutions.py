"""Lesson 9 Solutions"""
from typing import Any, Literal, Optional, TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command, interrupt


class DocumentState(TypedDict, total=False):
    title: str
    content: str
    word_count: int
    status: Optional[Literal["draft", "review", "approved", "rejected"]]
    reviewer_notes: str


def draft_document(state: DocumentState) -> dict[str, Any]:
    content = state.get("content") or ""
    return {"word_count": len(content.split()), "status": "draft"}


def request_review(state: DocumentState) -> Command[Literal["publish", "revise"]]:
    decision = interrupt({
        "question": "Approve this document?",
        "title": state.get("title") or "",
        "word_count": state.get("word_count") or 0,
    })
    update = {"reviewer_notes": decision.get("notes", ""), "status": "review"}
    if decision.get("approved"):
        return Command(goto="publish", update=update)
    else:
        return Command(goto="revise", update=update)


def publish(state: DocumentState) -> dict[str, Any]:
    return {"status": "approved"}


def revise(state: DocumentState) -> dict[str, Any]:
    return {"status": "rejected"}


def build_graph():
    graph = StateGraph(DocumentState)
    graph.add_node("draft_document", draft_document)
    graph.add_node("request_review", request_review)
    graph.add_node("publish", publish)
    graph.add_node("revise", revise)
    
    graph.add_edge(START, "draft_document")
    graph.add_edge("draft_document", "request_review")
    graph.add_edge("publish", END)
    graph.add_edge("revise", END)
    
    return graph.compile(checkpointer=MemorySaver())
