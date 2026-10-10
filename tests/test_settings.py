from research_agent.settings import load_settings


def test_load_settings_uses_defaults(monkeypatch):
    monkeypatch.delenv("RESEARCH_AGENT_SEARCH_MAX_RESULTS", raising=False)
    monkeypatch.delenv("RESEARCH_AGENT_PAGE_FETCH_TIMEOUT_SECONDS", raising=False)

    settings = load_settings()

    assert settings.search_max_results == 5
    assert settings.page_fetch_timeout_seconds == 10.0


def test_load_settings_reads_environment_variables(monkeypatch):
    monkeypatch.setenv("RESEARCH_AGENT_SEARCH_MAX_RESULTS", "3")
    monkeypatch.setenv("RESEARCH_AGENT_PAGE_FETCH_TIMEOUT_SECONDS", "4.5")

    settings = load_settings()

    assert settings.search_max_results == 3
    assert settings.page_fetch_timeout_seconds == 4.5
