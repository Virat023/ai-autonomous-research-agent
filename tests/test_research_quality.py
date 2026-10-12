import pytest

from research_agent import research


def test_research_topic_rejects_uncited_model_findings(monkeypatch):
    monkeypatch.setattr(
        research,
        "search_web",
        lambda query, max_results: [
            {
                "title": "Solar overview",
                "url": "https://example.com/solar",
                "snippet": "Solar panels convert sunlight to electricity.",
            }
        ],
    )
    monkeypatch.setattr(
        research,
        "extract_page_text",
        lambda url: "Solar panels convert sunlight to electricity.",
    )
    monkeypatch.setattr(
        research,
        "generate_response",
        lambda prompt: "Solar panels make electricity.",
    )

    with pytest.raises(
        RuntimeError,
        match="did not include source citations",
    ):
        research.research_topic("solar panels")
