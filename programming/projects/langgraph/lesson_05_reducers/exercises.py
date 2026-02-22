"""Lesson 5 Exercises: Reducers & State Accumulation

Build a pipeline with append and custom reducers. Run tests with:
    uv run pytest tests/test_lesson_05.py -v
"""
import operator
from typing import Annotated, Any, TypedDict

from langgraph.graph import StateGraph, START, END


# --- Exercise 1: Define state with reducers ---
# Define ResearchState with:
#   - query: str (no reducer, plain field)
#   - sources: Annotated[list[dict], operator.add]  (append reducer)
#   - keywords: Annotated[list[str], operator.add]   (append reducer)
#   - relevance_score: float (no reducer, last-write-wins)

class ResearchState(TypedDict, total=False):
    # TODO: Define fields with appropriate reducers
    ...


# --- Exercise 2: Write nodes that use append reducers ---

def extract_keywords(state: ResearchState) -> dict[str, Any]:
    """Extract keywords from the query.
    
    Split query into words, keep words longer than 3 characters, lowercase.
    Return dict with keywords list.
    
    Example: "How do I process refunds" → ["process", "refunds"]
    """
    # TODO: Implement
    ...


def search_web(state: ResearchState) -> dict[str, Any]:
    """Simulate web search. Return sources with web results.
    
    Return:
    - sources: [{"source": "web", "title": "Web result for: <query>"}]
    - relevance_score: 0.7
    """
    # TODO: Implement
    ...


def search_docs(state: ResearchState) -> dict[str, Any]:
    """Simulate documentation search. Return sources with doc results.
    
    Return:
    - sources: [{"source": "docs", "title": "Doc result for: <query>"}]
    - relevance_score: 0.9
    
    Note: relevance_score has no reducer, so this will overwrite web's 0.7
    """
    # TODO: Implement
    ...


# --- Exercise 3: Custom reducer ---

def min_reducer(current: float, new: float) -> float:
    """Keep the LOWER value. Opposite of max_reducer.
    
    Useful for "minimum confidence" tracking.
    """
    # TODO: Implement (one line)
    ...


# --- Exercise 4: Build the pipeline ---

def build_pipeline():
    """Build: extract_keywords → search_web → search_docs
    
    Wire linearly: START → extract_keywords → search_web → search_docs → END
    """
    # TODO: Implement
    ...
