"""Lesson 7 Exercises: Error Handling

Build resilient nodes with graceful degradation. Run tests with:
    uv run pytest tests/test_lesson_07.py -v
"""
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


# --- Exercise 1: Graceful degradation ---

def analyze_text(state: AnalysisState) -> dict[str, Any]:
    """Analyze text with graceful degradation.
    
    In the try block:
    1. Get text from state (default "")
    2. If text is empty, raise ValueError("Empty text")
    3. Count words → word_count
    4. If word_count > 20 → category = "long", confidence = 0.9
       If word_count > 5 → category = "medium", confidence = 0.8
       Else → category = "short", confidence = 0.7
    5. Return dict with word_count, category, confidence
    
    In the except block:
    - Log a warning with logger.warning()
    - Return fallback: word_count=0, category="unknown", confidence=0.0
    """
    # TODO: Implement with try/except
    ...


# --- Exercise 2: Fail-closed gate ---

def approval_gate(state: AnalysisState) -> dict[str, Any]:
    """Gate that blocks low-confidence analyses.
    
    In the try block:
    - If confidence >= 0.75 → is_approved=True, block_reason=""
    - If confidence < 0.75 → is_approved=False, block_reason="Low confidence: {confidence}"
    
    In the except block (FAIL-CLOSED):
    - is_approved=False, block_reason="Gate error: {error message}"
    """
    # TODO: Implement
    ...


def route_after_gate(state: AnalysisState) -> str:
    """Route: approved → summarize, blocked → END."""
    # TODO: Implement
    ...


# --- Exercise 3: Response node ---

def summarize(state: AnalysisState) -> dict[str, Any]:
    """Generate summary.
    
    Format: "Analysis: {category} text ({word_count} words, {confidence:.0%} confidence)"
    Return dict with summary field.
    """
    # TODO: Implement
    ...


# --- Exercise 4: Build the graph ---

def build_graph():
    """Build: analyze_text → approval_gate → [conditional] → summarize → END
    
    Add RetryPolicy to analyze_text: max_attempts=3, backoff_factor=2.0
    Add conditional edges after approval_gate.
    """
    # TODO: Implement
    ...
