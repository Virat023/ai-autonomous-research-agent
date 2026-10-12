from research_agent import research


def test_research_topic_builds_report_with_source_citations(monkeypatch):
    captured = {}

    monkeypatch.setattr(
        research,
        "search_web",
        lambda query, max_results: [
            {
                "title": "Climate overview",
                "url": "https://example.com/climate",
                "snippet": "A short climate summary.",
            }
        ],
    )
    monkeypatch.setattr(
        research,
        "extract_page_text",
        lambda url: "Average temperatures are rising.",
    )

    def fake_generate_response(prompt):
        captured["prompt"] = prompt
        return "## Summary\nAverage temperatures are rising [1]."

    monkeypatch.setattr(research, "generate_response", fake_generate_response)

    report = research.research_topic("  climate change  ")

    assert "Average temperatures are rising [1]." in report
    assert "[1] Climate overview - https://example.com/climate" in report
    assert "Average temperatures are rising." in captured["prompt"]
    assert "climate change" in captured["prompt"]

