import pytest

from research_agent import search


def test_search_web_returns_title_url_and_snippet(monkeypatch):
    class FakeDDGS:
        def text(self, query, max_results):
            assert query == "climate change"
            assert max_results == 2
            return [
                {
                    "title": "Example source",
                    "href": "https://example.com",
                    "body": "A short description.",
                }
            ]

    monkeypatch.setattr(search, "DDGS", lambda: FakeDDGS())

    results = search.search_web("  climate change  ", max_results=2)

    assert results == [
        {
            "title": "Example source",
            "url": "https://example.com",
            "snippet": "A short description.",
        }
    ]


def test_search_web_replaces_long_title_with_domain_and_deduplicates(monkeypatch):
    url = "https://www.example.com/article"

    class FakeDDGS:
        def text(self, query, max_results):
            return [
                {
                    "title": "A concatenated title " * 10,
                    "href": url,
                    "body": "A description.",
                },
                {
                    "title": "Duplicate result",
                    "href": url,
                    "body": "Duplicate description.",
                },
            ]

    monkeypatch.setattr(search, "DDGS", lambda: FakeDDGS())

    results = search.search_web("example topic")

    assert results == [
        {
            "title": "example.com",
            "url": url,
            "snippet": "A description.",
        }
    ]


def test_search_web_rejects_blank_query():
    with pytest.raises(ValueError, match="Search query cannot be blank."):
        search.search_web("   ")