"""Capstone Edges: Routing logic for the mini support pipeline."""
from langgraph.graph import END


def route_after_triage(state: dict) -> str:
    """Route after triage: spam→END, urgent/normal→classify."""
    if state.get("force_continue"):
        return "classify_intent"
    ticket_type = state.get("ticket_type") or "normal"
    if ticket_type == "spam":
        return END
    return "classify_intent"


def route_after_gate(state: dict) -> str:
    """Route after quality gate: approved→END (done), blocked→END."""
    # Both paths end, but we track the decision in state
    return END
