"""Lesson 5: Reducers & State Accumulation

Understand how LangGraph merges state updates. Key concepts:
1. Default: last-write-wins (plain fields)
2. Annotated[list[str], operator.add] — append instead of replace
3. Custom reducer functions
4. Why reducers matter: parallel nodes writing to the same field

Echo Pattern: Evidence lists use append reducers so that multiple retrieval
nodes can each contribute evidence without overwriting each other.
"""
import operator
from typing import Annotated, Any, TypedDict

from langgraph.graph import StateGraph, START, END


# --- 1. Default behavior: last-write-wins ---

class BasicState(TypedDict, total=False):
    value: str
    items: list[str]  # No reducer — last write wins!

def node_a(state: BasicState) -> dict[str, Any]:
    return {"value": "from_a", "items": ["a1", "a2"]}

def node_b(state: BasicState) -> dict[str, Any]:
    return {"value": "from_b", "items": ["b1"]}

# If both write to "items", node_b's value replaces node_a's completely.
# This is the DEFAULT behavior.


# --- 2. Annotated + operator.add: append reducer ---

class AccumulatorState(TypedDict, total=False):
    query: str
    tags: Annotated[list[str], operator.add]      # Append items
    evidence: Annotated[list[dict], operator.add]  # Append dicts
    score: float  # No reducer — last-write-wins

def tag_keywords(state: AccumulatorState) -> dict[str, Any]:
    """Extract keyword tags from the query."""
    query = (state.get("query") or "").lower()
    tags = []
    if "refund" in query:
        tags.append("refund")
    if "urgent" in query:
        tags.append("urgent")
    if not tags:
        tags.append("general")
    return {"tags": tags}  # These get APPENDED to existing tags

def find_faq_evidence(state: AccumulatorState) -> dict[str, Any]:
    """Find FAQ-based evidence."""
    return {
        "evidence": [{"source": "faq", "text": "Refunds take 5-7 business days"}],
        "score": 0.8,
    }

def find_policy_evidence(state: AccumulatorState) -> dict[str, Any]:
    """Find policy-based evidence."""
    return {
        "evidence": [{"source": "policy", "text": "Full refund within 30 days"}],
        "score": 0.9,  # This REPLACES the previous score (no reducer)
    }


# --- 3. Custom reducer function ---

def max_reducer(current: float, new: float) -> float:
    """Keep the higher value. Useful for escalation-only scores."""
    return max(current, new)

class CustomReducerState(TypedDict, total=False):
    query: str
    risk_score: Annotated[float, max_reducer]  # Can only go UP
    notes: Annotated[list[str], operator.add]


def assess_content(state: CustomReducerState) -> dict[str, Any]:
    """Assess content risk."""
    return {"risk_score": 0.3, "notes": ["content assessed"]}

def assess_user(state: CustomReducerState) -> dict[str, Any]:
    """Assess user risk (higher score)."""
    return {"risk_score": 0.7, "notes": ["user history checked"]}

def assess_low(state: CustomReducerState) -> dict[str, Any]:
    """This tries to LOWER the score, but max_reducer prevents it."""
    return {"risk_score": 0.1, "notes": ["attempted lower score"]}


def demo_append_reducer():
    """Show how operator.add appends list items."""
    graph = StateGraph(AccumulatorState)
    graph.add_node("tag_keywords", tag_keywords)
    graph.add_node("find_faq", find_faq_evidence)
    graph.add_node("find_policy", find_policy_evidence)
    
    graph.add_edge(START, "tag_keywords")
    graph.add_edge("tag_keywords", "find_faq")
    graph.add_edge("find_faq", "find_policy")
    graph.add_edge("find_policy", END)
    
    app = graph.compile()
    result = app.invoke({"query": "I need an urgent refund", "tags": [], "evidence": []})
    
    print("=== Append Reducer Demo ===")
    print(f"  tags: {result['tags']}")  # ["refund", "urgent"] — appended
    print(f"  evidence: {len(result['evidence'])} items")  # 2 — both appended
    print(f"  score: {result['score']}")  # 0.9 — last-write-wins
    return result


def demo_custom_reducer():
    """Show how a custom max_reducer works."""
    graph = StateGraph(CustomReducerState)
    graph.add_node("assess_content", assess_content)
    graph.add_node("assess_user", assess_user)
    graph.add_node("assess_low", assess_low)
    
    graph.add_edge(START, "assess_content")
    graph.add_edge("assess_content", "assess_user")
    graph.add_edge("assess_user", "assess_low")
    graph.add_edge("assess_low", END)
    
    app = graph.compile()
    result = app.invoke({"query": "test", "risk_score": 0.0, "notes": []})
    
    print("\n=== Custom Reducer Demo ===")
    print(f"  risk_score: {result['risk_score']}")  # 0.7 — max wins, 0.1 was blocked
    print(f"  notes: {result['notes']}")  # All 3 notes appended
    return result


if __name__ == "__main__":
    demo_append_reducer()
    demo_custom_reducer()
