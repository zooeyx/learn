"""Lesson 4 Exercises: Conditional Routing

Build a graph with multiple routing paths. Run tests with:
    uv run pytest tests/test_lesson_04.py -v
"""
from typing import Any, TypedDict

from langgraph.graph import StateGraph, START, END


class ReviewState(TypedDict, total=False):
    text: str
    language: str
    sentiment: str
    response: str
    status: str
    force_continue: bool


# --- Exercise 1: Write a routing function ---

def route_after_detect(state: ReviewState) -> str:
    """Route based on detected language.
    
    Rules:
    - If force_continue is True → always return "analyze"
    - If language is "unknown" → return END (early exit)
    - If language is "en" → return "analyze"
    - Otherwise → return "translate" (non-English needs translation)
    """
    # TODO: Implement
    ...


# --- Exercise 2: Write node functions ---

def detect_language(state: ReviewState) -> dict[str, Any]:
    """Detect the language of the text.
    
    Simple rules (check text lowercase):
    - Contains "bonjour" or "merci" → language = "fr"
    - Contains "hola" or "gracias" → language = "es"
    - Contains only ASCII letters/spaces/punctuation → language = "en"
    - Otherwise → language = "unknown"
    
    Hint: You can check ASCII with text.isascii()
    """
    # TODO: Implement
    ...


def translate(state: ReviewState) -> dict[str, Any]:
    """Simulate translation to English.
    
    Return dict with text set to "[translated] " + original text.
    """
    # TODO: Implement
    ...


def analyze(state: ReviewState) -> dict[str, Any]:
    """Analyze sentiment of the text.
    
    Rules (check text lowercase):
    - Contains "great" or "love" or "excellent" → sentiment = "positive"
    - Contains "bad" or "hate" or "terrible" → sentiment = "negative"
    - Otherwise → sentiment = "neutral"
    """
    # TODO: Implement
    ...


def create_response(state: ReviewState) -> dict[str, Any]:
    """Generate a response based on sentiment.
    
    - "positive" → response = "Thank you for your kind words!", status = "resolved"
    - "negative" → response = "We're sorry. We'll improve.", status = "needs_followup"
    - otherwise → response = "Thank you for your feedback.", status = "resolved"
    """
    # TODO: Implement
    ...


# --- Exercise 3: Build the graph ---

def build_graph():
    """Build a graph with conditional routing.
    
    Structure:
    START → detect_language → [conditional routing]
        - END (unknown language, early exit)
        - translate → analyze → create_response → END
        - analyze → create_response → END
    """
    # TODO: Implement
    ...
