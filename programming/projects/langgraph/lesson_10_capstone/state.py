"""Capstone State: Mini Support-Ticket Pipeline

TypedDict state with ~15 fields, governance-style annotations.
Combines patterns from all previous lessons.
"""
import operator
from typing import Annotated, Any, Literal, TypedDict


def max_risk(current: str, new: str) -> str:
    """Escalation-only reducer: risk can only go UP."""
    levels = {"low": 0, "medium": 1, "high": 2}
    current_level = levels.get(current, 0)
    new_level = levels.get(new, 0)
    return new if new_level > current_level else current


class TicketState(TypedDict, total=False):
    # Input
    query: str
    channel: str  # "email" or "chat"

    # Triage
    ticket_type: str  # "spam", "urgent", "normal"
    is_spam: bool

    # Classification (parallel node 1)
    intent: str
    confidence: float

    # Context extraction (parallel node 2)
    entities: Annotated[list[str], operator.add]
    context_summary: str

    # Evidence
    evidence: Annotated[list[dict], operator.add]
    evidence_score: float

    # Draft
    draft: str
    quality_score: float

    # Gate
    is_approved: bool
    block_reason: str
    risk_level: Annotated[str, max_risk]  # Escalation-only

    # Debug
    force_continue: bool
