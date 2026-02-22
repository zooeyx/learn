"""Lesson 7: Error Handling & Graceful Degradation

Build resilient nodes that never crash the pipeline. Key concepts:
1. try/except with fallback return values
2. RetryPolicy(max_attempts=3, backoff_factor=2.0, jitter=True)
3. Fail-closed gate pattern: exception = block, not pass
4. Logging with structured fields

Echo Pattern: Every node catches exceptions and returns safe fallback values.
Gates (pre-generation checkpoints) are fail-closed: if anything goes wrong,
they BLOCK the pipeline rather than letting bad data through.
"""
import logging
from typing import Any, TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.types import RetryPolicy

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


class TicketState(TypedDict, total=False):
    query: str
    intent: str
    confidence: float
    is_allowed: bool
    block_reason: str
    response: str


# --- 1. Graceful degradation with try/except ---

call_count = 0  # Track calls for demo

def classify_with_fallback(state: TicketState) -> dict[str, Any]:
    """Node that gracefully degrades on failure.
    
    Echo Pattern: catch exceptions, return fallback, don't crash.
    """
    query = state.get("query") or ""
    
    try:
        # Simulate an LLM call that might fail
        global call_count
        call_count += 1
        if call_count % 2 == 0:
            raise ConnectionError("LLM API timeout")
        
        # Success path
        intent = "billing" if "refund" in query.lower() else "general"
        logger.info("classify.complete intent=%s confidence=0.95", intent)
        return {"intent": intent, "confidence": 0.95}
    
    except Exception as e:
        # Fallback path — safe defaults, not a crash
        logger.warning("classify.failed error=%s", str(e))
        return {"intent": "general", "confidence": 0.0}


# --- 2. Fail-closed gate ---

def quality_gate(state: TicketState) -> dict[str, Any]:
    """Gate that BLOCKS on failure (fail-closed).
    
    Echo's safety naming convention:
    - gate: pre-generation checkpoint (blocks pipeline)
    - guard: post-generation filter
    - guardrails: external safety service
    
    Fail-closed means: if we CAN'T check, we BLOCK.
    This is the opposite of fail-open (if we can't check, we allow).
    """
    try:
        confidence = state.get("confidence") or 0.0
        
        if confidence < 0.5:
            return {
                "is_allowed": False,
                "block_reason": f"Low confidence: {confidence:.2f}",
            }
        
        return {"is_allowed": True, "block_reason": ""}
    
    except Exception as e:
        # FAIL-CLOSED: exception means BLOCK, not PASS
        logger.warning("quality_gate.failed error=%s — blocking", str(e))
        return {
            "is_allowed": False,
            "block_reason": f"Gate error: {str(e)}",
        }


def route_after_gate(state: TicketState) -> str:
    """Route based on gate decision."""
    if state.get("is_allowed"):
        return "respond"
    return END  # Blocked — exit pipeline


def respond(state: TicketState) -> dict[str, Any]:
    """Generate response (only reached if gate passes)."""
    intent = state.get("intent") or "general"
    return {"response": f"Handling your {intent} request."}


# --- 3. RetryPolicy ---

def unreliable_node(state: TicketState) -> dict[str, Any]:
    """A node that sometimes fails — RetryPolicy will retry it."""
    import random
    if random.random() < 0.3:
        raise ConnectionError("Transient failure")
    return {"intent": "classified"}


def build_graph_with_retry():
    """Build a graph with RetryPolicy on an unreliable node."""
    graph = StateGraph(TicketState)
    
    # Add node WITH retry policy — LangGraph retries automatically
    graph.add_node(
        "classify",
        unreliable_node,
        retry_policy=RetryPolicy(max_attempts=3, backoff_factor=2.0),
    )
    graph.add_node("respond", respond)
    
    graph.add_edge(START, "classify")
    graph.add_edge("classify", "respond")
    graph.add_edge("respond", END)
    
    return graph.compile()


def build_graph_with_gate():
    """Build a graph with fail-closed gate."""
    graph = StateGraph(TicketState)
    
    graph.add_node("classify", classify_with_fallback)
    graph.add_node("quality_gate", quality_gate)
    graph.add_node("respond", respond)
    
    graph.add_edge(START, "classify")
    graph.add_edge("classify", "quality_gate")
    graph.add_conditional_edges(
        "quality_gate",
        route_after_gate,
        {"respond": "respond", END: END},
    )
    graph.add_edge("respond", END)
    
    return graph.compile()


if __name__ == "__main__":
    print("=== Graceful Degradation + Gate Demo ===")
    app = build_graph_with_gate()
    
    # First call succeeds (call_count becomes 1, odd → success)
    call_count = 0
    print("\nCall 1 (should succeed):")
    result = app.invoke({"query": "I need a refund"})
    print(f"  is_allowed={result.get('is_allowed')}, response={result.get('response')}")
    
    # Second call fails (call_count becomes 2, even → error → fallback → low confidence → blocked)
    print("\nCall 2 (LLM fails → fallback → gate blocks):")
    result = app.invoke({"query": "I need a refund"})
    print(f"  is_allowed={result.get('is_allowed')}, block_reason={result.get('block_reason')}")
