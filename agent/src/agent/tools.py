import requests
from ddgs import DDGS
from bs4 import BeautifulSoup
from agents import function_tool


@function_tool
def scrape_page(url: str, max_chars: int = 3000):
    """
    Fetch and clean text content from a web page.
    """
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        html = requests.get(url, headers=headers, timeout=10).text
        soup = BeautifulSoup(html, "html.parser")
        paragraphs = [p.text for p in soup.find_all("p")]
        text = " ".join(paragraphs)
        print(f"Tool 'scrape_page' Result: {text[:max_chars]}")
        return text[:max_chars]
    except Exception as e:
        return f"Error scraping {url}: {e}"


@function_tool
def search_web(query: str, max_results: int = 5):
    """
    Search the web using DuckDuckGo and return a list of result URLs.
    """
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=max_results):
            if "href" in r:
                results.append(r["href"])
    print(f"Tools 'search_web' Result: {results}")
    return results
