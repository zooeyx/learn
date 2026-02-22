"""Lesson 9: Checkpointing & Persistence

Save and resume pipeline state. Key concepts:
1. MemorySaver / InMemorySaver — in-memory checkpointer
2. config = {"configurable": {"thread_id": "..."}} — scoping
3. Resume from checkpoint (same thread_id picks up where left off)
4. interrupt() to pause, Command(resume=...) to continue (human-in-the-loop)

Echo Pattern: The email pipeline uses PostgreSQL checkpointing for production
and MemorySaver for tests. Thread IDs scope state per conversation/ticket.
"""
from typing import Any, Literal, Optional, TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.types import Command, interrupt


# === Part 1: Basic Checkpointing ===

class CounterState(TypedDict, total=False):
    count: int
    log: str


def increment(state: CounterState) -> dict[str, Any]:
    """Increment the counter."""
    count = (state.get("count") or 0) + 1
    print(f"  [increment] count={count}")
    return {"count": count, "log": f"incremented to {count}"}


def build_counter_graph():
    """Build a simple graph with checkpointing."""
    graph = StateGraph(CounterState)
    graph.add_node("increment", increment)
    graph.add_edge(START, "increment")
    graph.add_edge("increment", END)
    
    # Compile WITH a checkpointer
    checkpointer = MemorySaver()
    return graph.compile(checkpointer=checkpointer)


def demo_checkpointing():
    """Show how thread_id scopes state across invocations."""
    app = build_counter_graph()
    
    # Thread 1: separate state
    config1 = {"configurable": {"thread_id": "thread-1"}}
    config2 = {"configurable": {"thread_id": "thread-2"}}
    
    print("=== Checkpointing Demo ===\n")
    
    print("Thread 1, invoke 1:")
    result = app.invoke({"count": 0}, config1)
    print(f"  Result: count={result['count']}\n")
    
    print("Thread 2, invoke 1:")
    result = app.invoke({"count": 10}, config2)
    print(f"  Result: count={result['count']}\n")
    
    # Get the state for thread 1
    state1 = app.get_state(config1)
    print(f"Thread 1 saved state: {state1.values}\n")
    
    state2 = app.get_state(config2)
    print(f"Thread 2 saved state: {state2.values}")


# === Part 2: Human-in-the-Loop with interrupt ===

class ApprovalState(TypedDict, total=False):
    request: str
    amount: float
    status: Optional[Literal["pending", "approved", "rejected"]]
    reason: str


def review_request(state: ApprovalState) -> Command[Literal["approve", "reject"]]:
    """Pause for human review using interrupt().
    
    interrupt() pauses the graph and surfaces data to the caller.
    When resumed with Command(resume=...), the value passed to resume
    becomes the return value of interrupt().
    """
    decision = interrupt({
        "question": "Approve this request?",
        "request": state["request"],
        "amount": state["amount"],
    })
    
    # After resume, decision contains whatever was passed to Command(resume=...)
    if decision:
        return Command(goto="approve")
    else:
        return Command(goto="reject")


def approve(state: ApprovalState) -> dict[str, Any]:
    return {"status": "approved", "reason": "Manager approved"}


def reject(state: ApprovalState) -> dict[str, Any]:
    return {"status": "rejected", "reason": "Manager rejected"}


def build_approval_graph():
    graph = StateGraph(ApprovalState)
    graph.add_node("review_request", review_request)
    graph.add_node("approve", approve)
    graph.add_node("reject", reject)
    
    graph.add_edge(START, "review_request")
    graph.add_edge("approve", END)
    graph.add_edge("reject", END)
    
    return graph.compile(checkpointer=MemorySaver())


def demo_human_in_the_loop():
    """Show interrupt/resume flow."""
    app = build_approval_graph()
    config = {"configurable": {"thread_id": "approval-1"}}
    
    print("\n\n=== Human-in-the-Loop Demo ===\n")
    
    # First invoke — hits interrupt, pauses
    print("Submitting request (will pause at review):")
    result = app.invoke(
        {"request": "Purchase new server", "amount": 5000.0, "status": "pending"},
        config=config,
    )
    # result will have __interrupt__ key
    print(f"  Paused. Interrupt data: {result.get('__interrupt__', 'N/A')}")
    
    # Check current state
    state = app.get_state(config)
    print(f"  Current status: {state.values.get('status')}")
    
    # Resume with approval
    print("\nResuming with approval (decision=True):")
    result = app.invoke(Command(resume=True), config=config)
    print(f"  Final status: {result.get('status')}")
    print(f"  Reason: {result.get('reason')}")


if __name__ == "__main__":
    demo_checkpointing()
    demo_human_in_the_loop()
