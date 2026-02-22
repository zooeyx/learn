"""Capstone: Mini Support-Ticket Pipeline (6 nodes)

Combines all course patterns:
- TypedDict state with governance annotations (Lesson 1, 5)
- StateGraph with nodes and edges (Lesson 2, 3)
- Conditional routing and early exits (Lesson 4)
- Reducers for parallel-safe state (Lesson 5)
- LLM integration with structured output (Lesson 6)
- Graceful degradation and fail-closed gates (Lesson 7)
- Parallel fan-out / fan-in (Lesson 8)
- Checkpointing (Lesson 9)

Pipeline structure:
    triage → [conditional: spam→END]
         ↓
    [classify_intent ‖ extract_context]  (parallel)
         ↓
    build_evidence → generate_draft → quality_gate → END
"""
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.types import RetryPolicy

from lesson_10_capstone.state import TicketState
from lesson_10_capstone.nodes import (
    triage,
    classify_intent,
    extract_context,
    build_evidence,
    generate_draft,
    quality_gate,
)
from lesson_10_capstone.edges import route_after_triage


def build_pipeline(use_checkpointer: bool = False):
    """Build the capstone pipeline.

    Args:
        use_checkpointer: If True, compile with MemorySaver.
    """
    graph = StateGraph(TicketState)

    # Add nodes (with retry on LLM node)
    graph.add_node("triage", triage)
    graph.add_node(
        "classify_intent",
        classify_intent,
        retry_policy=RetryPolicy(max_attempts=3, backoff_factor=2.0),
    )
    graph.add_node("extract_context", extract_context)
    graph.add_node("build_evidence", build_evidence)
    graph.add_node("generate_draft", generate_draft)
    graph.add_node("quality_gate", quality_gate)

    # Edges
    graph.add_edge(START, "triage")

    # Conditional: triage routes spam→END or continues
    graph.add_conditional_edges(
        "triage",
        route_after_triage,
        {END: END, "classify_intent": "classify_intent"},
    )

    # Fan-out: classify + extract run in parallel
    graph.add_edge("classify_intent", "build_evidence")
    graph.add_edge("classify_intent", "extract_context")
    graph.add_edge("extract_context", "build_evidence")

    # Linear: evidence → draft → gate → END
    graph.add_edge("build_evidence", "generate_draft")
    graph.add_edge("generate_draft", "quality_gate")
    graph.add_edge("quality_gate", END)

    # Compile
    checkpointer = MemorySaver() if use_checkpointer else None
    return graph.compile(checkpointer=checkpointer)


if __name__ == "__main__":
    app = build_pipeline()

    print("=" * 60)
    print("CAPSTONE: Mini Support-Ticket Pipeline")
    print("=" * 60)

    print("\n--- Test 1: Normal billing ticket ---")
    result = app.invoke({
        "query": "I was charged twice for order #12345. Please refund.",
        "channel": "email",
        "entities": [],
        "evidence": [],
    })
    print(f"  Intent: {result.get('intent')} (confidence: {result.get('confidence', 0):.0%})")
    print(f"  Evidence: {len(result.get('evidence', []))} items")
    print(f"  Quality: {result.get('quality_score', 0):.2f}")
    print(f"  Approved: {result.get('is_approved')}")
    print(f"  Draft preview: {(result.get('draft') or '')[:80]}...")

    print("\n--- Test 2: Spam (early exit) ---")
    result = app.invoke({
        "query": "Buy now! Free money! Click here for deals!",
        "channel": "email",
        "entities": [],
        "evidence": [],
    })
    print(f"  Ticket type: {result.get('ticket_type')}")
    print(f"  Is spam: {result.get('is_spam')}")
    print(f"  Draft: {result.get('draft', 'N/A')}")

    print("\n--- Test 3: Urgent technical ticket ---")
    result = app.invoke({
        "query": "URGENT: The payment system is crashing for all users at Acme Corp",
        "channel": "chat",
        "entities": [],
        "evidence": [],
    })
    print(f"  Ticket type: {result.get('ticket_type')}")
    print(f"  Intent: {result.get('intent')}")
    print(f"  Risk level: {result.get('risk_level')}")
    print(f"  Entities: {result.get('entities')}")
    print(f"  Approved: {result.get('is_approved')}")

    print("\n--- Test 4: Low confidence (gate blocks) ---")
    result = app.invoke({
        "query": "hmm",
        "channel": "chat",
        "entities": [],
        "evidence": [],
    })
    print(f"  Intent: {result.get('intent')}")
    print(f"  Confidence: {result.get('confidence', 0):.2f}")
    print(f"  Approved: {result.get('is_approved')}")
    print(f"  Block reason: {result.get('block_reason')}")

    print("\n" + "=" * 60)
    print("All tests complete!")
