"""Lesson 8: Parallel Execution (Fan-out / Fan-in)

Run nodes concurrently with fan-out and fan-in. Key concepts:
1. Multiple edges from one node → LangGraph runs targets in parallel
2. Fan-in: parallel nodes converge to a single downstream node
3. Reducers ensure parallel writes merge correctly
4. LangGraph waits for ALL fan-out branches before continuing

Echo Pattern: The email pipeline runs customer_context and classify_intent
in parallel after triage, then converges at workflow_decider.
"""
import operator
from typing import Annotated, Any, TypedDict

from langgraph.graph import StateGraph, START, END


class TicketState(TypedDict, total=False):
    query: str
    entities: Annotated[list[str], operator.add]      # Parallel-safe: append
    tags: Annotated[list[str], operator.add]           # Parallel-safe: append
    sentiment: str
    entity_count: int
    priority: int
    summary: str


# --- Parallel nodes (fan-out) ---

def extract_entities(state: TicketState) -> dict[str, Any]:
    """Extract named entities from the query (runs in parallel)."""
    query = state.get("query") or ""
    words = query.split()
    # Simple heuristic: capitalized words are entities
    entities = [w for w in words if w[0:1].isupper()]
    print(f"  [extract_entities] Found: {entities}")
    return {
        "entities": entities,
        "entity_count": len(entities),
    }


def analyze_sentiment(state: TicketState) -> dict[str, Any]:
    """Analyze sentiment of the query (runs in parallel)."""
    query = (state.get("query") or "").lower()
    
    positive = sum(1 for w in ["happy", "great", "love", "thanks"] if w in query)
    negative = sum(1 for w in ["angry", "frustrated", "broken", "hate"] if w in query)
    
    if positive > negative:
        sentiment = "positive"
    elif negative > positive:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    print(f"  [analyze_sentiment] {sentiment}")
    return {"sentiment": sentiment, "tags": [f"sentiment:{sentiment}"]}


# --- Convergence node (fan-in) ---

def score_priority(state: TicketState) -> dict[str, Any]:
    """Score priority using results from BOTH parallel nodes."""
    sentiment = state.get("sentiment") or "neutral"
    entity_count = state.get("entity_count") or 0
    
    # Higher priority for negative sentiment or many entities
    if sentiment == "negative":
        priority = 1
    elif entity_count > 3:
        priority = 2
    else:
        priority = 3
    
    print(f"  [score_priority] priority={priority}")
    return {"priority": priority}


def summarize(state: TicketState) -> dict[str, Any]:
    """Create a summary from the fully enriched state."""
    return {
        "summary": (
            f"Priority {state.get('priority')}: "
            f"{state.get('sentiment')} sentiment, "
            f"{state.get('entity_count')} entities, "
            f"tags={state.get('tags')}"
        )
    }


def build_graph():
    """Build a graph with parallel fan-out and fan-in.
    
    Structure:
        START → extract_entities ──┐
        START → analyze_sentiment ─┤
                                   └→ score_priority → summarize → END
    """
    graph = StateGraph(TicketState)
    
    graph.add_node("extract_entities", extract_entities)
    graph.add_node("analyze_sentiment", analyze_sentiment)
    graph.add_node("score_priority", score_priority)
    graph.add_node("summarize", summarize)
    
    # Fan-out: START goes to BOTH parallel nodes
    graph.add_edge(START, "extract_entities")
    graph.add_edge(START, "analyze_sentiment")
    
    # Fan-in: both parallel nodes go to score_priority
    graph.add_edge("extract_entities", "score_priority")
    graph.add_edge("analyze_sentiment", "score_priority")
    
    # Continue linearly
    graph.add_edge("score_priority", "summarize")
    graph.add_edge("summarize", END)
    
    return graph.compile()


if __name__ == "__main__":
    app = build_graph()
    
    print("=== Parallel Fan-out / Fan-in ===\n")
    
    print("Test 1: Negative sentiment")
    result = app.invoke({
        "query": "I am frustrated with the broken App by Acme Corp",
        "entities": [],
        "tags": [],
    })
    print(f"  Summary: {result['summary']}\n")
    
    print("Test 2: Many entities")
    result = app.invoke({
        "query": "Alice from Acme Corp contacted Bob at Widget Inc about the Tokyo project",
        "entities": [],
        "tags": [],
    })
    print(f"  Summary: {result['summary']}")
