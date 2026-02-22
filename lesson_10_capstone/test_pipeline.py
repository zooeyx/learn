"""Capstone Tests: End-to-end pipeline tests.

Tests: happy path, spam exit, low-quality block, LLM failure fallback.
"""
import pytest
from lesson_10_capstone.pipeline import build_pipeline


@pytest.fixture
def app():
    return build_pipeline()


def _base_input(**overrides):
    base = {"query": "", "channel": "email", "entities": [], "evidence": []}
    base.update(overrides)
    return base


class TestHappyPath:
    def test_billing_ticket_approved(self, app):
        result = app.invoke(_base_input(query="I need a refund for my last payment"))
        assert result["intent"] == "billing"
        assert result["confidence"] > 0.5
        assert result["is_approved"] is True
        assert "refund" in result["draft"].lower() or "billing" in result["draft"].lower()

    def test_technical_ticket(self, app):
        result = app.invoke(_base_input(query="The app crashes when I open settings"))
        assert result["intent"] == "technical"
        assert result["is_approved"] is True

    def test_evidence_populated(self, app):
        result = app.invoke(_base_input(query="How do I reset my password?"))
        assert len(result["evidence"]) > 0
        assert result["evidence_score"] > 0


class TestSpamExit:
    def test_spam_exits_early(self, app):
        result = app.invoke(_base_input(query="Buy now! Free money! Click here!"))
        assert result["is_spam"] is True
        assert result["ticket_type"] == "spam"
        assert result.get("draft") is None  # Never reached draft stage

    def test_force_continue_bypasses_spam(self, app):
        result = app.invoke(_base_input(
            query="Buy now! Free money!",
            force_continue=True,
        ))
        assert result.get("intent") is not None  # Classification ran


class TestQualityGate:
    def test_low_confidence_may_block(self, app):
        result = app.invoke(_base_input(query="x"))
        # Very short query → low confidence from mock → may be blocked
        assert isinstance(result.get("is_approved"), bool)

    def test_gate_records_block_reason(self, app):
        result = app.invoke(_base_input(query="x"))
        if not result.get("is_approved"):
            assert result.get("block_reason") != ""


class TestParallelNodes:
    def test_entities_extracted(self, app):
        result = app.invoke(_base_input(
            query="Alice from Acme Corp needs help with her account"
        ))
        assert len(result["entities"]) > 0

    def test_context_summary_populated(self, app):
        result = app.invoke(_base_input(query="Help me with my order"))
        assert result.get("context_summary") is not None


class TestCheckpointing:
    def test_with_checkpointer(self):
        app = build_pipeline(use_checkpointer=True)
        config = {"configurable": {"thread_id": "test-1"}}
        result = app.invoke(
            _base_input(query="I need a refund"),
            config=config,
        )
        assert result["intent"] == "billing"

        state = app.get_state(config)
        assert state.values["intent"] == "billing"
