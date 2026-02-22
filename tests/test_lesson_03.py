"""Tests for Lesson 3: Multi-Node Pipeline"""


def test_parse_input():
    from lesson_03_multi_node.solutions import parse_input
    result = parse_input({"raw_input": "email: alice@test.com\norder: ORD-123\nI need help"})
    assert result["customer_email"] == "alice@test.com"
    assert result["order_id"] == "ORD-123"


def test_parse_input_missing():
    from lesson_03_multi_node.solutions import parse_input
    result = parse_input({"raw_input": "just some text"})
    assert result["customer_email"] == ""
    assert result["order_id"] == ""


def test_classify_issue():
    from lesson_03_multi_node.solutions import classify_issue
    assert classify_issue({"raw_input": "shipping is slow"})["issue_type"] == "shipping"
    assert classify_issue({"raw_input": "item is damaged"})["issue_type"] == "damaged"
    assert classify_issue({"raw_input": "wrong item sent"})["issue_type"] == "wrong_item"
    assert classify_issue({"raw_input": "hello"})["issue_type"] == "other"


def test_assess_urgency():
    from lesson_03_multi_node.solutions import assess_urgency
    assert assess_urgency({"issue_type": "damaged", "raw_input": "broken"})["urgency"] == 1
    assert assess_urgency({"issue_type": "shipping", "raw_input": "where is it"})["urgency"] == 2
    assert assess_urgency({"issue_type": "other", "raw_input": "urgent please"})["urgency"] == 1


def test_generate_response():
    from lesson_03_multi_node.solutions import generate_response
    result = generate_response({"order_id": "ORD-1", "issue_type": "shipping", "urgency": 2})
    assert "ORD-1" in result["response"]
    assert "shipping" in result["response"]


def test_full_pipeline():
    from lesson_03_multi_node.solutions import build_pipeline
    app = build_pipeline()
    result = app.invoke({"raw_input": "email: bob@test.com\norder: ORD-99\nMy item was damaged"})
    assert result["customer_email"] == "bob@test.com"
    assert result["order_id"] == "ORD-99"
    assert result["issue_type"] == "damaged"
    assert result["urgency"] == 1
    assert "ORD-99" in result["response"]
