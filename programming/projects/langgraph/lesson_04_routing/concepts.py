"""Lesson 4: Conditional Routing

Add branching logic with conditional edges. Key concepts:
1. Routing functions: def route(state) -> str returning node names or END
2. add_conditional_edges("node", route_fn, {option: target})
3. Early exits — exit pipeline when conditions aren't met
4. force_continue bypass flag for debugging

Echo Pattern: The email pipeline has conditional exits at triage, grounding,
verification_gate, and policy_gate. Each can terminate the pipeline early.
"""
from typing import Any, Literal, TypedDict

from langgraph.graph import StateGraph, START, END


class TicketState(TypedDict, total=False):
    query: str
    ticket_type: str
    category: str
    priority: int
    response: str
    status: str
    force_continue: bool  # Debug bypass flag (Echo pattern)


# --- Routing function ---
# Returns the name of the next node (or END to exit)

def route_after_triage(state: TicketState) -> str:
    """Route based on ticket_type. Returns a node name or END.
    
    Echo calls this pattern "conditional exits" — the pipeline can
    terminate early at multiple points.
    """
    # Debug bypass: skip routing, always continue
    if state.get("force_continue"):
        return "enrich"
    
    ticket_type = state.get("ticket_type") or ""
    
    if ticket_type == "spam":
        return END  # Early exit — don't process spam
    elif ticket_type == "urgent":
        return "escalate"
    else:
        return "enrich"


# --- Node functions ---

def triage(state: TicketState) -> dict[str, Any]:
    """Classify the ticket type for routing."""
    query = (state.get("query") or "").lower()
    
    if any(word in query for word in ["buy now", "click here", "free money"]):
        ticket_type = "spam"
    elif any(word in query for word in ["urgent", "emergency", "critical"]):
        ticket_type = "urgent"
    else:
        ticket_type = "normal"
    
    print(f"  [triage] ticket_type={ticket_type}")
    return {"ticket_type": ticket_type}


def escalate(state: TicketState) -> dict[str, Any]:
    """Handle urgent tickets."""
    print("  [escalate] Routing to urgent queue")
    return {
        "response": "Your ticket has been escalated to our urgent queue.",
        "status": "escalated",
        "priority": 1,
    }


def enrich(state: TicketState) -> dict[str, Any]:
    """Standard enrichment for normal tickets."""
    print("  [enrich] Processing normally")
    return {"category": "general", "priority": 3}


def respond(state: TicketState) -> dict[str, Any]:
    """Generate response for non-urgent tickets."""
    category = state.get("category") or "general"
    return {
        "response": f"Thank you for your {category} inquiry. We'll respond within 24h.",
        "status": "pending",
    }


def build_graph():
    """Build a graph with conditional routing after triage."""
    graph = StateGraph(TicketState)
    
    graph.add_node("triage", triage)
    graph.add_node("escalate", escalate)
    graph.add_node("enrich", enrich)
    graph.add_node("respond", respond)
    
    # START → triage
    graph.add_edge(START, "triage")
    
    # triage → conditional routing
    graph.add_conditional_edges(
        "triage",
        route_after_triage,
        {
            END: END,            # spam → exit
            "escalate": "escalate",  # urgent → escalate
            "enrich": "enrich",      # normal → enrich
        },
    )
    
    # escalate → END
    graph.add_edge("escalate", END)
    
    # enrich → respond → END
    graph.add_edge("enrich", "respond")
    graph.add_edge("respond", END)
    
    return graph.compile()


if __name__ == "__main__":
    app = build_graph()
    
    print("=== Normal ticket ===")
    result = app.invoke({"query": "How do I reset my password?"})
    print(f"  Status: {result.get('status')}, Response: {result.get('response')}\n")
    
    print("=== Spam ticket (early exit) ===")
    result = app.invoke({"query": "Buy now! Free money! Click here!"})
    print(f"  Status: {result.get('status')}, Response: {result.get('response')}\n")
    
    print("=== Urgent ticket ===")
    result = app.invoke({"query": "URGENT: System is down, critical failure"})
    print(f"  Status: {result.get('status')}, Priority: {result.get('priority')}\n")
    
    print("=== Force continue (debug bypass) ===")
    result = app.invoke({"query": "Buy now! Free money!", "force_continue": True})
    print(f"  Status: {result.get('status')} (spam was NOT filtered)")
