from research_agent import content


def test_extract_page_text_removes_non_content_sections(monkeypatch):
    class FakeResponse:
        text = """
        <html>
            <header>Site header</header>
            <main><h1>Research result</h1><p>Useful information.</p></main>
            <script>ignore this</script>
            <footer>Site footer</footer>
        </html>
        """

        def raise_for_status(self):
            pass

    def fake_get(url, timeout, follow_redirects):
        assert url == "https://example.com"
        assert timeout == 10.0
        assert follow_redirects is True
        return FakeResponse()

    monkeypatch.setattr(content.httpx, "get", fake_get)

    text = content.extract_page_text("https://example.com")

    assert text == "Research result Useful information."
