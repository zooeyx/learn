"""Capstone Nodes: All node functions for the mini support pipeline.

Combines patterns: graceful degradation, structured output, mock LLM,
parallel-safe reducers, and gate logic.
"""
import logging
import os
from typing import Any

from pydantic import BaseModel, Field

from lesson_10_capstone.state import TicketState

logger = logging.getLogger(__name__)


# --- Pydantic model for LLM structured output ---

class ClassifyOutput(BaseModel):
    intent: str = Field(description="billing, technical, account, or general")
    confidence: float = Field(description="0.0 to 1.0")


class _MockResult:
    """Plain object with .model_dump() — avoids Pydantic serialization warnings."""
    def __init__(self, **kwargs: Any):
        self.__dict__.update(kwargs)

    def model_dump(self) -> dict[str, Any]:
        return dict(self.__dict__)


class MockClassifierLLM:
    """Mock LLM for offline work."""
    def invoke(self, messages):
        content = messages[-1].content if hasattr(messages[-1], "content") else str(messages[-1])
        c = content.lower()
        if any(w in c for w in ["bug", "error", "crash", "broken"]):
            return _MockResult(intent="technical", confidence=0.88)
        elif any(w in c for w in ["refund", "payment", "charge", "invoice"]):
            return _MockResult(intent="billing", confidence=0.92)
        elif any(w in c for w in ["password", "login", "account"]):
            return _MockResult(intent="account", confidence=0.85)
        else:
            return _MockResult(intent="general", confidence=0.70)


def _get_classifier():
    if os.environ.get("OPENAI_API_KEY"):
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model="gpt-4o-mini", temperature=0).with_structured_output(ClassifyOutput)
    return MockClassifierLLM()


# --- Node functions ---

def triage(state: TicketState) -> dict[str, Any]:
    """Triage: detect spam and urgency."""
    query = (state.get("query") or "").lower()

    spam_words = ["buy now", "click here", "free money", "act now"]
    if any(w in query for w in spam_words):
        logger.info("triage.spam_detected")
        return {"ticket_type": "spam", "is_spam": True, "risk_level": "low"}

    urgent_words = ["urgent", "emergency", "critical", "asap"]
    if any(w in query for w in urgent_words):
        logger.info("triage.urgent")
        return {"ticket_type": "urgent", "is_spam": False, "risk_level": "high"}

    return {"ticket_type": "normal", "is_spam": False, "risk_level": "low"}


def classify_intent(state: TicketState) -> dict[str, Any]:
    """Classify intent using LLM with structured output (parallel node 1)."""
    query = state.get("query") or ""
    try:
        llm = _get_classifier()
        from langchain_core.messages import HumanMessage
        result = llm.invoke([HumanMessage(content=f"Classify this support ticket: {query}")])
        output = result.model_dump()
        logger.info("classify_intent.complete intent=%s confidence=%.2f", output["intent"], output["confidence"])
        return {"intent": output["intent"], "confidence": output["confidence"]}
    except Exception as e:
        logger.warning("classify_intent.failed error=%s", str(e))
        return {"intent": "general", "confidence": 0.0}


def extract_context(state: TicketState) -> dict[str, Any]:
    """Extract entities and context (parallel node 2)."""
    query = state.get("query") or ""
    words = query.split()
    entities = [w for w in words if len(w) > 1 and w[0].isupper()]
    summary = f"Extracted {len(entities)} entities from {len(words)}-word query"
    return {"entities": entities, "context_summary": summary}


def build_evidence(state: TicketState) -> dict[str, Any]:
    """Build evidence from intent and context."""
    intent = state.get("intent") or "general"
    query = (state.get("query") or "").lower()

    evidence_db = {
        "billing": [
            {"source": "faq", "text": "Refunds are processed within 5-7 business days."},
            {"source": "policy", "text": "Full refund within 30 days of purchase."},
        ],
        "technical": [
            {"source": "kb", "text": "Try clearing cache and restarting the application."},
        ],
        "account": [
            {"source": "faq", "text": "Password reset link sent to registered email."},
        ],
        "general": [
            {"source": "faq", "text": "Contact support@example.com for assistance."},
        ],
    }

    evidence = evidence_db.get(intent, evidence_db["general"])
    score = min(0.9, 0.5 + 0.1 * len(evidence))
    return {"evidence": evidence, "evidence_score": score}


def generate_draft(state: TicketState) -> dict[str, Any]:
    """Generate a draft response using evidence."""
    intent = state.get("intent") or "general"
    evidence = state.get("evidence") or []
    entities = state.get("entities") or []
    confidence = state.get("confidence") or 0.0

    evidence_text = "; ".join(e.get("text", "") for e in evidence[:2])

    draft = (
        f"Thank you for contacting us regarding your {intent} inquiry.\n\n"
        f"Based on our records: {evidence_text}\n\n"
    )

    if entities:
        draft += f"Reference: {', '.join(entities[:3])}\n\n"

    draft += "Please let us know if you need further assistance."

    quality = min(1.0, confidence * 0.5 + (0.1 * len(evidence)))
    return {"draft": draft, "quality_score": quality}


def quality_gate(state: TicketState) -> dict[str, Any]:
    """Gate: block low-quality drafts (fail-closed)."""
    try:
        quality = state.get("quality_score") or 0.0
        confidence = state.get("confidence") or 0.0
        evidence_score = state.get("evidence_score") or 0.0

        if quality < 0.3:
            return {"is_approved": False, "block_reason": f"Low quality: {quality:.2f}", "risk_level": "high"}

        if confidence < 0.3 and evidence_score < 0.5:
            return {"is_approved": False, "block_reason": "Low confidence and evidence", "risk_level": "medium"}

        return {"is_approved": True, "block_reason": ""}

    except Exception as e:
        logger.warning("quality_gate.failed error=%s — blocking", str(e))
        return {"is_approved": False, "block_reason": f"Gate error: {str(e)}", "risk_level": "high"}
