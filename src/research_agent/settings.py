import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    search_max_results: int
    page_fetch_timeout_seconds: float


def load_settings() -> Settings:
    return Settings(
        search_max_results=int(os.getenv("RESEARCH_AGENT_SEARCH_MAX_RESULTS", "5")),
        page_fetch_timeout_seconds=float(
            os.getenv("RESEARCH_AGENT_PAGE_FETCH_TIMEOUT_SECONDS", "10")
        ),
    )
