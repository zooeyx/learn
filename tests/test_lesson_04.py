"""Tests for Lesson 4: Conditional Routing"""


def test_detect_language_english():
    from lesson_04_routing.solutions import detect_language
    assert detect_language({"text": "This is great"})["language"] == "en"


def test_detect_language_french():
    from lesson_04_routing.solutions import detect_language
    assert detect_language({"text": "Bonjour, merci"})["language"] == "fr"


def test_detect_language_spanish():
    from lesson_04_routing.solutions import detect_language
    assert detect_language({"text": "Hola amigo"})["language"] == "es"


def test_route_after_detect_english():
    from lesson_04_routing.solutions import route_after_detect
    assert route_after_detect({"language": "en"}) == "analyze"


def test_route_after_detect_unknown():
    from lesson_04_routing.solutions import route_after_detect
    from langgraph.graph import END
    assert route_after_detect({"language": "unknown"}) == END


def test_route_after_detect_force_continue():
    from lesson_04_routing.solutions import route_after_detect
    assert route_after_detect({"language": "unknown", "force_continue": True}) == "analyze"


def test_route_after_detect_non_english():
    from lesson_04_routing.solutions import route_after_detect
    assert route_after_detect({"language": "fr"}) == "translate"


def test_translate():
    from lesson_04_routing.solutions import translate
    result = translate({"text": "Bonjour"})
    assert result["text"] == "[translated] Bonjour"


def test_analyze():
    from lesson_04_routing.solutions import analyze
    assert analyze({"text": "This is great"})["sentiment"] == "positive"
    assert analyze({"text": "This is terrible"})["sentiment"] == "negative"
    assert analyze({"text": "Hello"})["sentiment"] == "neutral"


def test_create_response():
    from lesson_04_routing.solutions import create_response
    pos = create_response({"sentiment": "positive"})
    assert pos["status"] == "resolved"
    neg = create_response({"sentiment": "negative"})
    assert neg["status"] == "needs_followup"


def test_full_graph_english():
    from lesson_04_routing.solutions import build_graph
    app = build_graph()
    result = app.invoke({"text": "I love this product, it's great!"})
    assert result["language"] == "en"
    assert result["sentiment"] == "positive"
    assert result["status"] == "resolved"


def test_full_graph_non_english():
    from lesson_04_routing.solutions import build_graph
    app = build_graph()
    result = app.invoke({"text": "Bonjour, great product"})
    assert result["language"] == "fr"
    assert "[translated]" in result["text"]
    assert result.get("sentiment") is not None


def test_full_graph_early_exit():
    from lesson_04_routing.solutions import build_graph
    app = build_graph()
    # Non-ASCII text → unknown language → early exit
    result = app.invoke({"text": "\u4f60\u597d"})  # Chinese characters
    assert result["language"] == "unknown"
    assert result.get("sentiment") is None  # Never reached analyze
