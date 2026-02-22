"""Tests for Lesson 6: LLM Integration"""
import os


def test_sentiment_output_model():
    from lesson_06_llm.solutions import SentimentOutput
    output = SentimentOutput(sentiment="positive", score=0.9, key_phrase="great")
    assert output.sentiment == "positive"
    assert output.score == 0.9
    d = output.model_dump()
    assert isinstance(d, dict)
    assert d["sentiment"] == "positive"


def test_mock_sentiment_llm_positive():
    from lesson_06_llm.solutions import MockSentimentLLM
    from langchain_core.messages import HumanMessage
    llm = MockSentimentLLM()
    result = llm.invoke([HumanMessage(content="I love this product!")])
    assert result.sentiment == "positive"
    assert result.score == 0.9


def test_mock_sentiment_llm_negative():
    from lesson_06_llm.solutions import MockSentimentLLM
    from langchain_core.messages import HumanMessage
    llm = MockSentimentLLM()
    result = llm.invoke([HumanMessage(content="I hate this terrible service")])
    assert result.sentiment == "negative"
    assert result.score == -0.8


def test_mock_sentiment_llm_neutral():
    from lesson_06_llm.solutions import MockSentimentLLM
    from langchain_core.messages import HumanMessage
    llm = MockSentimentLLM()
    result = llm.invoke([HumanMessage(content="The weather is cloudy")])
    assert result.sentiment == "neutral"


def test_analyze_sentiment_positive():
    # Force mock by ensuring no API key
    old_key = os.environ.pop("OPENAI_API_KEY", None)
    try:
        from lesson_06_llm.solutions import analyze_sentiment
        result = analyze_sentiment({"text": "I love this amazing product!"})
        assert result["sentiment"] == "positive"
        assert result["score"] == 0.9
    finally:
        if old_key:
            os.environ["OPENAI_API_KEY"] = old_key


def test_create_response_positive():
    from lesson_06_llm.solutions import create_response
    result = create_response({"score": 0.9})
    assert result["response"] == "Thank you for the positive feedback!"


def test_create_response_negative():
    from lesson_06_llm.solutions import create_response
    result = create_response({"score": -0.8})
    assert result["response"] == "We're sorry to hear that. We'll improve."


def test_create_response_neutral():
    from lesson_06_llm.solutions import create_response
    result = create_response({"score": 0.0})
    assert result["response"] == "Thank you for your feedback."


def test_full_graph():
    old_key = os.environ.pop("OPENAI_API_KEY", None)
    try:
        from lesson_06_llm.solutions import build_graph
        app = build_graph()
        result = app.invoke({"text": "I love this amazing service!"})
        assert result["sentiment"] == "positive"
        assert result["response"] == "Thank you for the positive feedback!"
    finally:
        if old_key:
            os.environ["OPENAI_API_KEY"] = old_key
