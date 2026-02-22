"""Lesson 3 Solutions"""
from typing import Any, TypedDict

from langgraph.graph import StateGraph, START, END


class OrderState(TypedDict, total=False):
    raw_input: str
    customer_email: str
    order_id: str
    issue_type: str
    urgency: int
    response: str


def parse_input(state: OrderState) -> dict[str, Any]:
    raw = state.get("raw_input") or ""
    email = ""
    order_id = ""
    for line in raw.split("\n"):
        line_lower = line.strip().lower()
        if line_lower.startswith("email:"):
            email = line.split(":", 1)[1].strip()
        elif line_lower.startswith("order:"):
            order_id = line.split(":", 1)[1].strip()
    return {"customer_email": email, "order_id": order_id}


def classify_issue(state: OrderState) -> dict[str, Any]:
    raw = (state.get("raw_input") or "").lower()
    if "shipping" in raw or "delivery" in raw:
        return {"issue_type": "shipping"}
    elif "damaged" in raw or "broken" in raw:
        return {"issue_type": "damaged"}
    elif "wrong" in raw or "incorrect" in raw:
        return {"issue_type": "wrong_item"}
    else:
        return {"issue_type": "other"}


def assess_urgency(state: OrderState) -> dict[str, Any]:
    issue = state.get("issue_type") or "other"
    raw = (state.get("raw_input") or "").lower()
    
    urgency_map = {"damaged": 1, "wrong_item": 2, "shipping": 2, "other": 3}
    urgency = urgency_map.get(issue, 3)
    
    if "urgent" in raw or "asap" in raw:
        urgency = 1
    
    return {"urgency": urgency}


def generate_response(state: OrderState) -> dict[str, Any]:
    order_id = state.get("order_id") or "N/A"
    issue_type = state.get("issue_type") or "unknown"
    urgency = state.get("urgency") or 3
    
    response = (
        f"Dear customer,\n\n"
        f"Re: Order {order_id}\n"
        f"Issue: {issue_type} (urgency: {urgency})\n\n"
        f"We will resolve this promptly.\n\n"
        f"Support Team"
    )
    return {"response": response}


def build_pipeline():
    graph = StateGraph(OrderState)
    graph.add_node("parse_input", parse_input)
    graph.add_node("classify_issue", classify_issue)
    graph.add_node("assess_urgency", assess_urgency)
    graph.add_node("generate_response", generate_response)
    graph.add_edge(START, "parse_input")
    graph.add_edge("parse_input", "classify_issue")
    graph.add_edge("classify_issue", "assess_urgency")
    graph.add_edge("assess_urgency", "generate_response")
    graph.add_edge("generate_response", END)
    return graph.compile()
