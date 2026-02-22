"""Tests for Lesson 8: Parallel Execution"""


def test_count_words():
    from lesson_08_parallel.solutions import count_words
    result = count_words({"text": "hello world foo"})
    assert result["word_count"] == 3
    assert result["findings"] == ["word_count:3"]


def test_count_words_empty():
    from lesson_08_parallel.solutions import count_words
    result = count_words({})
    assert result["word_count"] == 0


def test_extract_keywords():
    from lesson_08_parallel.solutions import extract_keywords
    result = extract_keywords({"text": "The application crashed unexpectedly"})
    assert "application" in result["keywords"]
    assert "crashed" in result["keywords"]
    assert "unexpectedly" in result["keywords"]


def test_assess_reading_level_beginner():
    from lesson_08_parallel.solutions import assess_reading_level
    result = assess_reading_level({"text": "The cat sat on a mat"})
    assert result["reading_level"] == "beginner"


def test_assess_reading_level_advanced():
    from lesson_08_parallel.solutions import assess_reading_level
    result = assess_reading_level({"text": "Extraordinarily sophisticated implementation"})
    assert result["reading_level"] == "advanced"


def test_create_summary():
    from lesson_08_parallel.solutions import create_summary
    result = create_summary({
        "word_count": 10,
        "keywords": ["hello", "world"],
        "reading_level": "beginner",
    })
    assert "10 words" in result["summary"]
    assert "2 keywords" in result["summary"]
    assert "beginner" in result["summary"]


def test_full_graph_parallel():
    from lesson_08_parallel.solutions import build_graph
    app = build_graph()
    result = app.invoke({
        "text": "The extraordinarily sophisticated application crashed unexpectedly yesterday",
        "keywords": [],
        "findings": [],
    })
    assert result["word_count"] > 0
    assert len(result["keywords"]) > 0
    assert result["reading_level"] is not None
    assert result["summary"] is not None
    # All 3 parallel nodes should have contributed findings
    assert len(result["findings"]) == 3
