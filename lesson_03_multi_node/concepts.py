"""Lesson 3: Multi-Node Linear Pipeline

Chain 4 nodes into a linear pipeline. Key concepts:
1. State grows richer as it flows through nodes
2. Each node reads what it needs, returns only what it changes
3. Pattern: state.get("field") or default for safe access
4. Nodes: ingest → enrich → score → respond

Echo Pattern: The email pipeline has 20 nodes in a linear chain.
Each node reads from state, does focused work, and returns a partial update.
"""
from typing import Any, TypedDict

from langgraph.graph import StateGraph, START, END


class TicketState(TypedDict, total=False):
    raw_input: str
    query: str
    customer_name: str
    category: str
    priority: int
    priority_label: str
    response: str


def ingest(state: TicketState) -> dict[str, Any]:
    """Node 1: Parse raw input into structured fields."""
    raw = state.get("raw_input") or ""
    
    # Simple parsing: first line is name, rest is query
    lines = raw.strip().split("\n")
    name = lines[0].strip() if lines else "Unknown"
    query = "\n".join(lines[1:]).strip() if len(lines) > 1 else raw.strip()
    
    print(f"  [ingest] name={name!r}, query={query!r}")
    return {"customer_name": name, "query": query}


def enrich(state: TicketState) -> dict[str, Any]:
    """Node 2: Categorize the ticket based on keywords."""
    query = (state.get("query") or "").lower()
    
    categories = {
        "billing": ["refund", "payment", "charge", "invoice"],
        "technical": ["bug", "error", "crash", "broken"],
        "account": ["password", "login", "access", "locked"],
    }
    
    for cat, keywords in categories.items():
        if any(kw in query for kw in keywords):
            print(f"  [enrich] category={cat}")
            return {"category": cat}
    
    print("  [enrich] category=general")
    return {"category": "general"}


def score(state: TicketState) -> dict[str, Any]:
    """Node 3: Assign priority based on category and keywords."""
    category = state.get("category") or "general"
    query = (state.get("query") or "").lower()
    
    # Base priority by category
    priority_map = {"billing": 2, "technical": 2, "account": 1, "general": 3}
    priority = priority_map.get(category, 3)
    
    # Escalate for urgent keywords
    if any(word in query for word in ["urgent", "asap", "immediately"]):
        priority = 1
    
    labels = {1: "urgent", 2: "normal", 3: "low"}
    label = labels.get(priority, "low")
    
    print(f"  [score] priority={priority} ({label})")
    return {"priority": priority, "priority_label": label}


def respond(state: TicketState) -> dict[str, Any]:
    """Node 4: Generate a template response."""
    name = state.get("customer_name") or "Customer"
    category = state.get("category") or "general"
    priority_label = state.get("priority_label") or "normal"
    
    response = (
        f"Hi {name},\n\n"
        f"We received your {category} ticket (priority: {priority_label}). "
        f"A specialist will follow up shortly.\n\n"
        f"Best regards,\nSupport Team"
    )
    
    print(f"  [respond] Generated response ({len(response)} chars)")
    return {"response": response}


def build_pipeline():
    """Build a 4-node linear pipeline: ingest → enrich → score → respond"""
    graph = StateGraph(TicketState)
    
    graph.add_node("ingest", ingest)
    graph.add_node("enrich", enrich)
    graph.add_node("score", score)
    graph.add_node("respond", respond)
    
    graph.add_edge(START, "ingest")
    graph.add_edge("ingest", "enrich")
    graph.add_edge("enrich", "score")
    graph.add_edge("score", "respond")
    graph.add_edge("respond", END)
    
    return graph.compile()


if __name__ == "__main__":
    app = build_pipeline()
    
    print("=== Billing Ticket ===")
    result = app.invoke({
        "raw_input": "Alice Johnson\nI need a refund for my last payment"
    })
    print(f"\n  Final state keys: {list(result.keys())}")
    print(f"  Response:\n{result['response']}\n")
    
    print("=== Urgent Technical Ticket ===")
    result = app.invoke({
        "raw_input": "Bob Smith\nThe app is crashing urgently, please fix immediately"
    })
    print(f"\n  Priority: {result['priority']} ({result['priority_label']})")
    print(f"  Response:\n{result['response']}")
