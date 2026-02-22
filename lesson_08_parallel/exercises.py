"""Lesson 8 Exercises: Parallel Execution

Build a pipeline with fan-out / fan-in. Run tests with:
    uv run pytest tests/test_lesson_08.py -v
"""
import operator
from typing import Annotated, Any, TypedDict

from langgraph.graph import StateGraph, START, END


# --- Exercise 1: Define state with parallel-safe fields ---

class ArticleState(TypedDict, total=False):
    text: str
    word_count: int
    keywords: Annotated[list[str], operator.add]   # Parallel-safe
    findings: Annotated[list[str], operator.add]    # Parallel-safe
    reading_level: str
    summary: str


# --- Exercise 2: Write parallel nodes ---

def count_words(state: ArticleState) -> dict[str, Any]:
    """Count words in the text.
    
    Return dict with:
    - word_count: number of words
    - findings: ["word_count:{count}"] (uses append reducer)
    """
    # TODO: Implement
    ...


def extract_keywords(state: ArticleState) -> dict[str, Any]:
    """Extract keywords (words longer than 5 chars, lowercase, unique).
    
    Return dict with:
    - keywords: list of unique long words
    - findings: ["keywords:{count}"] where count is len(keywords)
    """
    # TODO: Implement
    ...


def assess_reading_level(state: ArticleState) -> dict[str, Any]:
    """Assess reading level based on average word length.
    
    Calculate average word length from text.
    - avg > 7 → "advanced"
    - avg > 5 → "intermediate" 
    - else → "beginner"
    
    Return dict with:
    - reading_level: the level string
    - findings: ["reading_level:{level}"]
    """
    # TODO: Implement
    ...


# --- Exercise 3: Convergence node ---

def create_summary(state: ArticleState) -> dict[str, Any]:
    """Create summary using results from all parallel nodes.
    
    Format: "{word_count} words, {len(keywords)} keywords, {reading_level} level"
    Return dict with summary.
    """
    # TODO: Implement
    ...


# --- Exercise 4: Build the parallel graph ---

def build_graph():
    """Build a graph with 3-way fan-out and fan-in.
    
    Structure:
        START → count_words ────────────┐
        START → extract_keywords ───────┤
        START → assess_reading_level ───┤
                                        └→ create_summary → END
    """
    # TODO: Implement
    ...
