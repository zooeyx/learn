"""Lesson 3 Exercises: Multi-Node Pipeline

Build a 4-node ticket processing pipeline. Run tests with:
    uv run pytest tests/test_lesson_03.py -v
"""
from typing import Any, TypedDict

from langgraph.graph import StateGraph, START, END


# --- Exercise 1: Define the state ---
class OrderState(TypedDict, total=False):
    raw_input: str
    customer_email: str
    order_id: str
    issue_type: str
    urgency: int
    response: str


# --- Exercise 2: Write 4 node functions ---

def parse_input(state: OrderState) -> dict[str, Any]:
    """Node 1: Parse raw_input to extract customer_email and order_id.
    
    Format: "email: <email>\norder: <order_id>\n<rest is ignored>"
    
    Parse rules:
    - Find line starting with "email:" → extract and strip the value
    - Find line starting with "order:" → extract and strip the value
    - Default to "" if not found
    
    Return dict with customer_email and order_id.
    """
    # TODO: Implement
    ...


def classify_issue(state: OrderState) -> dict[str, Any]:
    """Node 2: Classify the issue type from raw_input content.
    
    Rules (check raw_input lowercase):
    - Contains "shipping" or "delivery" → issue_type = "shipping"
    - Contains "damaged" or "broken" → issue_type = "damaged"
    - Contains "wrong" or "incorrect" → issue_type = "wrong_item"
    - Otherwise → issue_type = "other"
    
    Return dict with issue_type.
    """
    # TODO: Implement
    ...


def assess_urgency(state: OrderState) -> dict[str, Any]:
    """Node 3: Assess urgency based on issue_type and raw_input.
    
    Base urgency by issue type:
    - "damaged" → 1 (high)
    - "wrong_item" → 2 (medium)
    - "shipping" → 2 (medium)
    - "other" → 3 (low)
    
    Boost: if "urgent" or "asap" appears in raw_input (lowercase), set to 1.
    
    Return dict with urgency.
    """
    # TODO: Implement
    ...


def generate_response(state: OrderState) -> dict[str, Any]:
    """Node 4: Generate a response based on the processed state.
    
    Format:
    "Dear customer,\n\n"
    "Re: Order {order_id}\n"
    "Issue: {issue_type} (urgency: {urgency})\n\n"
    "We will resolve this promptly.\n\n"
    "Support Team"
    
    Use state.get() with sensible defaults for missing fields.
    Return dict with response.
    """
    # TODO: Implement
    ...


# --- Exercise 3: Build the pipeline ---

def build_pipeline():
    """Build a 4-node pipeline: parse_input → classify_issue → assess_urgency → generate_response
    
    Steps:
    1. Create StateGraph(OrderState)
    2. Add all 4 nodes
    3. Wire linear edges: START → parse → classify → assess → respond → END
    4. Compile and return
    """
    # TODO: Implement
    ...
