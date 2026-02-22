"""Tests for Lesson 5: Reducers"""


def test_extract_keywords():
    from lesson_05_reducers.solutions import extract_keywords
    result = extract_keywords({"query": "How do I process refunds quickly"})
    assert "process" in result["keywords"]
    assert "refunds" in result["keywords"]
    assert "quickly" in result["keywords"]
    # Short words excluded
    assert "How" not in result["keywords"]
    assert "do" not in result["keywords"]


def test_search_web():
    from lesson_05_reducers.solutions import search_web
    result = search_web({"query": "test query"})
    assert len(result["sources"]) == 1
    assert result["sources"][0]["source"] == "web"
    assert result["relevance_score"] == 0.7


def test_search_docs():
    from lesson_05_reducers.solutions import search_docs
    result = search_docs({"query": "test query"})
    assert len(result["sources"]) == 1
    assert result["sources"][0]["source"] == "docs"
    assert result["relevance_score"] == 0.9


def test_min_reducer():
    from lesson_05_reducers.solutions import min_reducer
    assert min_reducer(0.5, 0.3) == 0.3
    assert min_reducer(0.2, 0.8) == 0.2


def test_full_pipeline_sources_append():
    from lesson_05_reducers.solutions import build_pipeline
    app = build_pipeline()
    result = app.invoke({"query": "How to process refunds", "sources": [], "keywords": []})
    # Both search nodes should have appended their sources
    assert len(result["sources"]) == 2
    sources_types = [s["source"] for s in result["sources"]]
    assert "web" in sources_types
    assert "docs" in sources_types


def test_full_pipeline_keywords_append():
    from lesson_05_reducers.solutions import build_pipeline
    app = build_pipeline()
    result = app.invoke({"query": "Process customer refunds", "sources": [], "keywords": []})
    assert len(result["keywords"]) > 0


def test_full_pipeline_relevance_last_write_wins():
    from lesson_05_reducers.solutions import build_pipeline
    app = build_pipeline()
    result = app.invoke({"query": "test", "sources": [], "keywords": []})
    # search_docs runs after search_web, so relevance_score = 0.9
    assert result["relevance_score"] == 0.9
