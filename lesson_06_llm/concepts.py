"""Lesson 6: LLM Integration with Structured Output

Connect real LLM calls with structured output. Key concepts:
1. ChatOpenAI(model="gpt-4o-mini") — basic LLM setup
2. .with_structured_output(PydanticModel) — typed responses
3. Pydantic at boundary, TypedDict inside (Echo pattern)
4. .model_dump() to convert Pydantic → dict for state
5. Mock fallback for offline work

Echo Pattern: Pydantic models are used at API boundaries (input validation,
LLM structured output) but pipeline state is always TypedDict. Use .model_dump()
to cross the boundary.
"""
import os
from typing import Any, TypedDict

from pydantic import BaseModel, Field

from langgraph.graph import StateGraph, START, END


# --- Pydantic model for structured LLM output ---

class ClassifyOutput(BaseModel):
    """Structured output from the classification LLM call."""
    intent: str = Field(description="The classified intent: billing, technical, account, or general")
    confidence: float = Field(description="Confidence score from 0.0 to 1.0")
    reasoning: str = Field(description="Brief explanation of the classification")


# --- Mock LLM for offline work ---

class _MockResult:
    """Plain object with .model_dump() — avoids Pydantic serialization warnings
    that occur when LangGraph checkpoints encounter raw Pydantic models."""
    def __init__(self, **kwargs: Any):
        self.__dict__.update(kwargs)

    def model_dump(self) -> dict[str, Any]:
        return dict(self.__dict__)


class MockStructuredLLM:
    """Drop-in replacement when no API key is available."""

    def invoke(self, messages):
        # Extract the query from the last message
        content = messages[-1].content if hasattr(messages[-1], 'content') else str(messages[-1])
        content_lower = content.lower()

        if any(w in content_lower for w in ["refund", "payment", "charge"]):
            return _MockResult(intent="billing", confidence=0.92, reasoning="Contains billing keywords")
        elif any(w in content_lower for w in ["bug", "error", "crash"]):
            return _MockResult(intent="technical", confidence=0.88, reasoning="Contains technical keywords")
        elif any(w in content_lower for w in ["password", "login", "account"]):
            return _MockResult(intent="account", confidence=0.85, reasoning="Contains account keywords")
        else:
            return _MockResult(intent="general", confidence=0.70, reasoning="No specific domain detected")


def get_classifier_llm():
    """Get the classification LLM — real or mock based on API key availability."""
    api_key = os.environ.get("OPENAI_API_KEY")
    
    if api_key:
        from langchain_openai import ChatOpenAI
        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        return llm.with_structured_output(ClassifyOutput)
    else:
        print("  [No OPENAI_API_KEY found — using mock LLM]")
        return MockStructuredLLM()


# --- Pipeline state (TypedDict, not Pydantic) ---

class TicketState(TypedDict, total=False):
    query: str
    intent: str
    confidence: float
    reasoning: str
    response: str


# --- Node functions ---

def classify(state: TicketState) -> dict[str, Any]:
    """Classify the ticket using LLM with structured output.
    
    This demonstrates the Pydantic-at-boundary pattern:
    1. LLM returns a Pydantic model (ClassifyOutput)
    2. We convert to dict with .model_dump()
    3. State stays as TypedDict
    """
    query = state.get("query") or ""
    
    llm = get_classifier_llm()
    
    from langchain_core.messages import HumanMessage
    result = llm.invoke([HumanMessage(content=f"Classify this support ticket: {query}")])
    
    # Pydantic → dict (crossing the boundary)
    output = result.model_dump()
    
    print(f"  [classify] intent={output['intent']}, confidence={output['confidence']:.2f}")
    return {
        "intent": output["intent"],
        "confidence": output["confidence"],
        "reasoning": output["reasoning"],
    }


def respond(state: TicketState) -> dict[str, Any]:
    """Generate response based on classification."""
    intent = state.get("intent") or "general"
    confidence = state.get("confidence") or 0.0
    
    responses = {
        "billing": "I'll connect you with our billing department.",
        "technical": "Let me look into this technical issue.",
        "account": "I can help with your account access.",
        "general": "Thank you for contacting support.",
    }
    
    response = responses.get(intent, responses["general"])
    if confidence < 0.8:
        response += " (Note: I'm not fully certain about the category.)"
    
    return {"response": response}


def build_graph():
    graph = StateGraph(TicketState)
    graph.add_node("classify", classify)
    graph.add_node("respond", respond)
    graph.add_edge(START, "classify")
    graph.add_edge("classify", "respond")
    graph.add_edge("respond", END)
    return graph.compile()


if __name__ == "__main__":
    app = build_graph()
    
    print("=== Billing Query ===")
    result = app.invoke({"query": "I was charged twice for my subscription"})
    print(f"  Intent: {result['intent']} ({result['confidence']:.0%})")
    print(f"  Response: {result['response']}\n")
    
    print("=== Technical Query ===")
    result = app.invoke({"query": "The app crashes when I open settings"})
    print(f"  Intent: {result['intent']} ({result['confidence']:.0%})")
    print(f"  Response: {result['response']}")
