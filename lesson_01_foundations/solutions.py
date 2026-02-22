"""Lesson 1 Solutions"""
import asyncio
from typing import Any, Annotated, TypedDict


class TicketState(TypedDict, total=False):
    query: str
    category: str
    priority: int
    sentiment: str
    response: str


def get_priority_label(state: TicketState) -> str:
    priority = state.get("priority") or 3
    if priority == 1:
        return "urgent"
    elif priority == 2:
        return "normal"
    else:
        return "low"


def classify_sentiment(state: TicketState) -> dict[str, Any]:
    query = (state.get("query") or "").lower()
    if "angry" in query or "frustrated" in query:
        return {"sentiment": "negative"}
    elif "thank" in query or "happy" in query:
        return {"sentiment": "positive"}
    else:
        return {"sentiment": "neutral"}


async def enrich_ticket(state: TicketState) -> dict[str, Any]:
    query = (state.get("query") or "").lower()
    await asyncio.sleep(0.01)
    if "refund" in query or "payment" in query:
        return {"category": "billing", "priority": 1}
    elif "bug" in query or "error" in query:
        return {"category": "technical", "priority": 2}
    else:
        return {"category": "general", "priority": 3}


async def process_ticket(query: str) -> TicketState:
    state: TicketState = {"query": query}
    update = await enrich_ticket(state)
    state = {**state, **update}
    update2 = classify_sentiment(state)
    state = {**state, **update2}
    return state
