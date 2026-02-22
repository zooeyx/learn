"""Lesson 2: Your First LangGraph Graph

Build and run a 2-node graph. Key concepts:
1. StateGraph(State) — creating a graph with a state schema
2. add_node("name", fn) — registering node functions  
3. add_edge(START, "name") — wiring nodes together
4. graph.compile() → app.invoke() — running the graph

Echo Pattern: Each node receives the full state and returns a partial update dict.
LangGraph merges the update into state automatically.
"""
from typing import Any, TypedDict

from langgraph.graph import StateGraph, START, END


# --- Define the state schema ---
class TicketState(TypedDict, total=False):
    query: str
    normalized_query: str
    category: str


# --- Define node functions ---
# Each node takes state, returns a partial update dict

def normalize(state: TicketState) -> dict[str, Any]:
    """Node 1: Normalize the input query."""
    query = state.get("query") or ""
    cleaned = query.strip().lower()
    print(f"  [normalize] '{query}' → '{cleaned}'")
    return {"normalized_query": cleaned}


def classify(state: TicketState) -> dict[str, Any]:
    """Node 2: Classify the normalized query."""
    query = state.get("normalized_query") or ""
    
    words = query.split()
    if any(word in words for word in ["hello", "hi", "hey"]):
        category = "greeting"
    elif "?" in query:
        category = "question"
    else:
        category = "complaint"
    
    print(f"  [classify] '{query}' → category={category}")
    return {"category": category}


# --- Build the graph ---
def build_graph():
    """Build a 2-node graph: normalize → classify"""
    
    # 1. Create a StateGraph with the state schema
    graph = StateGraph(TicketState)
    
    # 2. Add nodes — each is a (name, function) pair
    graph.add_node("normalize", normalize)
    graph.add_node("classify", classify)
    
    # 3. Wire the edges: START → normalize → classify → END
    graph.add_edge(START, "normalize")
    graph.add_edge("normalize", "classify")
    graph.add_edge("classify", END)
    
    # 4. Compile into a runnable app
    return graph.compile()


# --- Run it ---
if __name__ == "__main__":
    app = build_graph()
    
    print("=== Test 1: Greeting ===")
    result = app.invoke({"query": "  Hello there!  "})
    print(f"  Result: {result}\n")
    
    print("=== Test 2: Question ===")
    result = app.invoke({"query": "How do I get a refund?"})
    print(f"  Result: {result}\n")
    
    print("=== Test 3: Complaint ===")
    result = app.invoke({"query": "This is broken"})
    print(f"  Result: {result}")
