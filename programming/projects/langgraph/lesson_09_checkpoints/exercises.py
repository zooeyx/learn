"""Lesson 9 Exercises: Checkpointing & Persistence

Build a pipeline with checkpointing and human-in-the-loop. Run tests with:
    uv run pytest tests/test_lesson_09.py -v
"""
from typing import Any, Literal, Optional, TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command, interrupt


# --- Exercise 1: State with checkpointing ---

class DocumentState(TypedDict, total=False):
    title: str
    content: str
    word_count: int
    status: Optional[Literal["draft", "review", "approved", "rejected"]]
    reviewer_notes: str


# --- Exercise 2: Node functions ---

def draft_document(state: DocumentState) -> dict[str, Any]:
    """Prepare a document for review.
    
    Set word_count from content (count words).
    Set status to "draft".
    Return dict with word_count and status.
    """
    # TODO: Implement
    ...


def request_review(state: DocumentState) -> Command[Literal["publish", "revise"]]:
    """Pause for human review using interrupt.
    
    1. Call interrupt() with a dict containing:
       - "question": "Approve this document?"
       - "title": state title
       - "word_count": state word_count
    2. The interrupt returns the reviewer's decision (a dict with "approved" bool and "notes" str)
    3. If decision["approved"] is True → Command(goto="publish", update={"reviewer_notes": decision["notes"], "status": "review"})
    4. If False → Command(goto="revise", update={"reviewer_notes": decision["notes"], "status": "review"})
    """
    # TODO: Implement
    ...


def publish(state: DocumentState) -> dict[str, Any]:
    """Mark document as approved.
    Return dict with status="approved".
    """
    # TODO: Implement
    ...


def revise(state: DocumentState) -> dict[str, Any]:
    """Mark document as rejected.
    Return dict with status="rejected".
    """
    # TODO: Implement
    ...


# --- Exercise 3: Build the graph with checkpointing ---

def build_graph():
    """Build a document review graph with checkpointing.
    
    Structure:
    START → draft_document → request_review → [approve: publish, reject: revise] → END
    
    Must compile with MemorySaver() checkpointer.
    """
    # TODO: Implement
    ...
