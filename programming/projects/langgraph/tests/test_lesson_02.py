"""Tests for Lesson 2: Your First Graph"""


def test_message_state_fields():
    from lesson_02_first_graph.solutions import MessageState
    state: MessageState = {"text": "hello", "word_count": 1, "is_long": False}
    assert state["text"] == "hello"


def test_count_words():
    from lesson_02_first_graph.solutions import count_words
    assert count_words({"text": "hello world"}) == {"word_count": 2}
    assert count_words({}) == {"word_count": 0}
    assert count_words({"text": ""}) == {"word_count": 0}


def test_check_length():
    from lesson_02_first_graph.solutions import check_length
    assert check_length({"word_count": 15}) == {"is_long": True}
    assert check_length({"word_count": 5}) == {"is_long": False}
    assert check_length({}) == {"is_long": False}


def test_build_graph_short():
    from lesson_02_first_graph.solutions import build_graph
    app = build_graph()
    result = app.invoke({"text": "hello world"})
    assert result["word_count"] == 2
    assert result["is_long"] is False


def test_build_graph_long():
    from lesson_02_first_graph.solutions import build_graph
    app = build_graph()
    result = app.invoke({"text": " ".join(["word"] * 15)})
    assert result["word_count"] == 15
    assert result["is_long"] is True
