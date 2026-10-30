from urllib.parse import urlsplit

from ddgs import DDGS


def search_web(query: str, max_results: int = 5) -> list[dict[str, str]]:
    """Search the web and return cleaned titles, URLs, and descriptions."""
    cleaned_query = query.strip()
    if not cleaned_query:
        raise ValueError("Search query cannot be blank.")

    results = DDGS().text(cleaned_query, max_results=max_results)
    cleaned_results = []
    seen_urls = set()

    for result in results:
        url = str(result.get("href") or "").strip()
        if not url or url in seen_urls:
            continue
        seen_urls.add(url)

        title = " ".join(str(result.get("title") or "").split())
        if not title or len(title) > 120:
            title = urlsplit(url).netloc.removeprefix("www.") or url

        snippet = " ".join(str(result.get("body") or "").split())

        cleaned_results.append(
            {
                "title": title,
                "url": url,
                "snippet": snippet,
            }
        )

    return cleaned_results