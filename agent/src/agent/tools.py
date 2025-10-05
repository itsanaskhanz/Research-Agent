from agents import function_tool


@function_tool
def scrape_page():
    """
    Fetch and clean text content from a web page.
    """
    return "Content Fetched"


@function_tool
def search_web():
    """
    Search the web using DuckDuckGo and return a list of result URLs.
    """
    return 'List of result URLs'
