"""Lesson 2 Exercises: Your First Graph

Build a 2-node LangGraph graph. Run tests with:
    uv run pytest tests/test_lesson_02.py -v
"""
from typing import Any, TypedDict

from langgraph.graph import StateGraph, START, END


# --- Exercise 1: Define the state ---
# Define MessageState with total=False containing:
#   - text: str
#   - word_count: int
#   - is_long: bool

# TODO: Define MessageState
class MessageState(TypedDict, total=False):
    ...  # Replace with field definitions


# --- Exercise 2: Write node functions ---

def count_words(state: MessageState) -> dict[str, Any]:
    """Count the words in state["text"].
    
    Return a dict with word_count set to the number of words.
    Handle missing/empty text by returning word_count=0.
    """
    # TODO: Implement
    ...


def check_length(state: MessageState) -> dict[str, Any]:
    """Check if the message is long (more than 10 words).
    
    Return a dict with is_long set to True/False.
    """
    # TODO: Implement
    ...


# --- Exercise 3: Build and compile the graph ---

def build_graph():
    """Build a graph: count_words → check_length
    
    Steps:
    1. Create StateGraph(MessageState)
    2. Add both nodes
    3. Wire: START → count_words → check_length → END
    4. Compile and return
    """
    # TODO: Implement
    ...
