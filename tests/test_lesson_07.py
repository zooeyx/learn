"""Tests for Lesson 7: Error Handling"""


def test_analyze_text_long():
    from lesson_07_errors.solutions import analyze_text
    text = " ".join(["word"] * 25)
    result = analyze_text({"text": text})
    assert result["word_count"] == 25
    assert result["category"] == "long"
    assert result["confidence"] == 0.9


def test_analyze_text_medium():
    from lesson_07_errors.solutions import analyze_text
    result = analyze_text({"text": "This is a medium length text with words"})
    assert result["category"] == "medium"
    assert result["confidence"] == 0.8


def test_analyze_text_short():
    from lesson_07_errors.solutions import analyze_text
    result = analyze_text({"text": "Hello world"})
    assert result["category"] == "short"
    assert result["confidence"] == 0.7


def test_analyze_text_empty_fallback():
    from lesson_07_errors.solutions import analyze_text
    result = analyze_text({})
    assert result["word_count"] == 0
    assert result["category"] == "unknown"
    assert result["confidence"] == 0.0


def test_approval_gate_approved():
    from lesson_07_errors.solutions import approval_gate
    result = approval_gate({"confidence": 0.9})
    assert result["is_approved"] is True
    assert result["block_reason"] == ""


def test_approval_gate_blocked():
    from lesson_07_errors.solutions import approval_gate
    result = approval_gate({"confidence": 0.3})
    assert result["is_approved"] is False
    assert "Low confidence" in result["block_reason"]


def test_approval_gate_fail_closed():
    from lesson_07_errors.solutions import approval_gate
    # Pass something that could cause issues
    result = approval_gate({})
    assert result["is_approved"] is False  # No confidence → 0.0 → blocked


def test_route_after_gate():
    from lesson_07_errors.solutions import route_after_gate
    from langgraph.graph import END
    assert route_after_gate({"is_approved": True}) == "summarize"
    assert route_after_gate({"is_approved": False}) == END


def test_summarize():
    from lesson_07_errors.solutions import summarize
    result = summarize({"category": "long", "word_count": 25, "confidence": 0.9})
    assert "long" in result["summary"]
    assert "25" in result["summary"]
    assert "90%" in result["summary"]


def test_full_graph_approved():
    from lesson_07_errors.solutions import build_graph
    app = build_graph()
    text = " ".join(["word"] * 25)
    result = app.invoke({"text": text})
    assert result["is_approved"] is True
    assert result.get("summary") is not None


def test_full_graph_blocked():
    from lesson_07_errors.solutions import build_graph
    app = build_graph()
    result = app.invoke({})  # Empty → fallback → low confidence → blocked
    assert result["is_approved"] is False
    assert result.get("summary") is None  # Never reached
