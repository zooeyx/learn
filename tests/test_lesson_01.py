"""Tests for Lesson 1: Python Foundations"""
import asyncio
import pytest


def test_ticket_state_is_typeddict():
    from lesson_01_foundations.solutions import TicketState
    # TypedDict creates a dict at runtime
    state: TicketState = {"query": "test"}
    assert isinstance(state, dict)
    assert state["query"] == "test"


def test_ticket_state_partial():
    from lesson_01_foundations.solutions import TicketState
    state: TicketState = {"query": "hello"}
    assert state.get("category") is None  # Missing field returns None


def test_get_priority_label():
    from lesson_01_foundations.solutions import get_priority_label
    assert get_priority_label({"priority": 1}) == "urgent"
    assert get_priority_label({"priority": 2}) == "normal"
    assert get_priority_label({"priority": 3}) == "low"
    assert get_priority_label({}) == "low"  # Missing → default


def test_classify_sentiment():
    from lesson_01_foundations.solutions import classify_sentiment
    assert classify_sentiment({"query": "I am angry"}) == {"sentiment": "negative"}
    assert classify_sentiment({"query": "Thank you!"}) == {"sentiment": "positive"}
    assert classify_sentiment({"query": "Hello"}) == {"sentiment": "neutral"}
    assert classify_sentiment({}) == {"sentiment": "neutral"}


async def test_enrich_ticket():
    from lesson_01_foundations.solutions import enrich_ticket
    result = await enrich_ticket({"query": "I need a refund"})
    assert result["category"] == "billing"
    assert result["priority"] == 1


async def test_enrich_ticket_technical():
    from lesson_01_foundations.solutions import enrich_ticket
    result = await enrich_ticket({"query": "There is a bug"})
    assert result["category"] == "technical"
    assert result["priority"] == 2


async def test_process_ticket():
    from lesson_01_foundations.solutions import process_ticket
    result = await process_ticket("I am angry about a refund")
    assert result["query"] == "I am angry about a refund"
    assert result["category"] == "billing"
    assert result["priority"] == 1
    assert result["sentiment"] == "negative"
