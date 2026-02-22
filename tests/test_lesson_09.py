"""Tests for Lesson 9: Checkpointing"""
from langgraph.types import Command


def test_draft_document():
    from lesson_09_checkpoints.solutions import draft_document
    result = draft_document({"content": "Hello world this is a test"})
    assert result["word_count"] == 6
    assert result["status"] == "draft"


def test_draft_document_empty():
    from lesson_09_checkpoints.solutions import draft_document
    result = draft_document({})
    assert result["word_count"] == 0
    assert result["status"] == "draft"


def test_publish():
    from lesson_09_checkpoints.solutions import publish
    assert publish({})["status"] == "approved"


def test_revise():
    from lesson_09_checkpoints.solutions import revise
    assert revise({})["status"] == "rejected"


def test_graph_with_checkpointing():
    from lesson_09_checkpoints.solutions import build_graph
    app = build_graph()
    config = {"configurable": {"thread_id": "test-doc-1"}}

    # First invoke — pauses at interrupt
    result = app.invoke(
        {"title": "Test Doc", "content": "Hello world this is a test document"},
        config=config,
    )
    # Should have hit the interrupt
    assert "__interrupt__" in result

    # Check saved state
    state = app.get_state(config)
    assert state.values["word_count"] == 7
    assert state.values["status"] == "draft"


def test_graph_approve():
    from lesson_09_checkpoints.solutions import build_graph
    app = build_graph()
    config = {"configurable": {"thread_id": "test-approve-1"}}

    # First invoke — pauses at interrupt
    app.invoke(
        {"title": "Good Doc", "content": "This is an excellent document for review"},
        config=config,
    )

    # Resume with approval
    result = app.invoke(
        Command(resume={"approved": True, "notes": "Looks good!"}),
        config=config,
    )
    assert result["status"] == "approved"
    assert result["reviewer_notes"] == "Looks good!"


def test_graph_reject():
    from lesson_09_checkpoints.solutions import build_graph
    app = build_graph()
    config = {"configurable": {"thread_id": "test-reject-1"}}

    # First invoke
    app.invoke(
        {"title": "Bad Doc", "content": "Needs work"},
        config=config,
    )

    # Resume with rejection
    result = app.invoke(
        Command(resume={"approved": False, "notes": "Too short"}),
        config=config,
    )
    assert result["status"] == "rejected"
    assert result["reviewer_notes"] == "Too short"


def test_separate_threads():
    from lesson_09_checkpoints.solutions import build_graph
    app = build_graph()
    config1 = {"configurable": {"thread_id": "thread-a"}}
    config2 = {"configurable": {"thread_id": "thread-b"}}

    app.invoke({"title": "Doc A", "content": "Short"}, config=config1)
    app.invoke({"title": "Doc B", "content": "A much longer document with more words"}, config=config2)

    state1 = app.get_state(config1)
    state2 = app.get_state(config2)

    assert state1.values["title"] == "Doc A"
    assert state2.values["title"] == "Doc B"
    assert state1.values["word_count"] != state2.values["word_count"]
