import httpx
from bs4 import BeautifulSoup


def extract_page_text(url: str) -> str:
    """Download a web page and return its readable text."""
    response = httpx.get(url, timeout=10.0, follow_redirects=True)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    for element in soup(["script", "style", "nav", "footer", "header", "noscript"]):
        element.decompose()

    return soup.get_text(" ", strip=True)
