"""Lesson 1: Python Foundations for Pipelines

Core Python features that LangGraph relies on:
1. TypedDict — structured dicts with type hints
2. total=False — all fields optional (partial updates)
3. Annotated[T, metadata] — attaching metadata to types  
4. async/await — basic coroutines
5. dict[str, Any] return pattern — why nodes return dicts

Echo Pattern: Pipeline nodes return dict[str, Any] with only changed fields.
LangGraph merges these partial updates into the full state automatically.
"""
import asyncio
from typing import Any, Annotated, TypedDict


# --- 1. TypedDict: structured dicts with type hints ---
# Unlike regular dicts, TypedDict lets you define exact keys and their types.
# This is how LangGraph defines pipeline state.

class TicketState(TypedDict, total=False):
    """A support ticket state. total=False means all fields are optional.
    
    Why total=False? LangGraph nodes return PARTIAL updates — only the fields
    they changed. The framework merges these into the full state.
    """
    query: str
    category: str
    priority: int
    response: str
    is_resolved: bool


# TypedDict instances are just regular dicts at runtime
ticket: TicketState = {"query": "I need a refund", "priority": 1}
print(f"1. TypedDict instance: {ticket}")
print(f"   Type at runtime: {type(ticket)}")  # <class 'dict'>

# Safe access with .get() — essential pattern for partial states
category = ticket.get("category") or "uncategorized"
print(f"   Safe access: category = {category!r}")


# --- 2. Annotated: attaching metadata to types ---
# Annotated lets you attach extra info to type hints without changing behavior.
# LangGraph uses this for reducers (how to merge state updates).

from typing import get_type_hints

class AnnotatedExample(TypedDict, total=False):
    name: str
    tags: Annotated[list[str], "append-reducer"]  # metadata says "append, don't replace"
    score: Annotated[float, "max-wins"]            # metadata says "keep the higher value"

# You can inspect annotations at runtime
hints = get_type_hints(AnnotatedExample, include_extras=True)
print(f"\n2. Annotated hints: {hints}")


# --- 3. async/await: basic coroutines ---
# LangGraph nodes can be async. This lets them make concurrent I/O calls
# (LLM APIs, database queries) without blocking.

async def fetch_customer_data(customer_id: str) -> dict[str, Any]:
    """Simulate an async API call."""
    await asyncio.sleep(0.01)  # Simulate network delay
    return {"customer_id": customer_id, "name": "Alice", "tier": "premium"}

async def enrich_ticket(state: TicketState) -> dict[str, Any]:
    """An async node function — the pattern every LangGraph node follows.
    
    Takes state, returns a partial update dict.
    """
    query = state.get("query") or ""
    
    # Simulate looking up customer info
    customer = await fetch_customer_data("C-123")
    
    return {
        "category": "billing" if "refund" in query.lower() else "general",
        "priority": 1 if customer["tier"] == "premium" else 3,
    }


# --- 4. The dict[str, Any] return pattern ---
# Every LangGraph node returns a dict with ONLY the fields it changed.
# This is a partial update — LangGraph merges it into the full state.

def classify_ticket(state: TicketState) -> dict[str, Any]:
    """Sync node — classify based on keywords."""
    query = state.get("query") or ""
    
    if "refund" in query.lower() or "money" in query.lower():
        return {"category": "billing", "priority": 1}
    elif "broken" in query.lower() or "error" in query.lower():
        return {"category": "technical", "priority": 2}
    else:
        return {"category": "general", "priority": 3}


# --- Running async code ---
async def main():
    state: TicketState = {"query": "I need a refund please"}
    print(f"\n3. Initial state: {state}")
    
    # Simulate a node running
    update = await enrich_ticket(state)
    print(f"   Node returned: {update}")
    
    # Merge update into state (this is what LangGraph does automatically)
    state = {**state, **update}
    print(f"   Merged state: {state}")
    
    # Sync node works the same way
    update2 = classify_ticket(state)
    print(f"\n4. Sync node returned: {update2}")


if __name__ == "__main__":
    asyncio.run(main())
