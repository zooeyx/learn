"""Lesson 1 Exercises: Python Foundations

Complete the TODOs below. Run tests with:
    uv run pytest tests/test_lesson_01.py -v
"""
import asyncio
from typing import Any, Annotated, TypedDict


# --- Exercise 1: Define a TypedDict ---
# Define a TicketState TypedDict with total=False containing these fields:
#   - query: str
#   - category: str  
#   - priority: int
#   - sentiment: str
#   - response: str

# TODO: Define TicketState here
class TicketState(TypedDict, total=False):
    ...  # Replace ... with the field definitions


# --- Exercise 2: Safe state access ---
def get_priority_label(state: TicketState) -> str:
    """Return a human-readable priority label.
    
    Rules:
    - priority 1 → "urgent"
    - priority 2 → "normal"  
    - priority 3 or missing → "low"
    
    Use state.get() for safe access (field might not exist).
    """
    # TODO: Implement this function
    ...


# --- Exercise 3: Partial state update function ---
def classify_sentiment(state: TicketState) -> dict[str, Any]:
    """Classify the sentiment of the ticket query.
    
    Rules (check query lowercase):
    - Contains "angry" or "frustrated" → sentiment = "negative"
    - Contains "thank" or "happy" → sentiment = "positive"
    - Otherwise → sentiment = "neutral"
    
    Return a dict with ONLY the sentiment field (partial update pattern).
    """
    # TODO: Implement this function
    ...


# --- Exercise 4: Async node function ---
async def enrich_ticket(state: TicketState) -> dict[str, Any]:
    """Async node that enriches a ticket.
    
    Steps:
    1. Get the query from state (default to empty string if missing)
    2. Simulate an async operation with: await asyncio.sleep(0.01)
    3. Set category based on query content:
       - "refund" or "payment" in query → category = "billing"
       - "bug" or "error" in query → category = "technical"
       - otherwise → category = "general"
    4. Set priority: billing=1, technical=2, general=3
    5. Return dict with category and priority
    """
    # TODO: Implement this function
    ...


# --- Exercise 5: Compose multiple updates ---
async def process_ticket(query: str) -> TicketState:
    """Process a ticket through multiple steps, merging updates.
    
    Steps:
    1. Create initial state with just the query
    2. Run enrich_ticket to get category and priority
    3. Merge the update into state (state = {**state, **update})
    4. Run classify_sentiment to get sentiment
    5. Merge that update too
    6. Return the final state
    """
    # TODO: Implement this function
    ...
