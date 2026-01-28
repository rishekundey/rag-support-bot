import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import deque
import json
from config import BASE_URL, MAX_PAGES, DATA_DIR

def crawl_website():
    visited = set()
    queue = deque([BASE_URL])
    pages = []

    while queue and len(pages) < MAX_PAGES:
        url = queue.popleft()
        if url in visited:
            continue

        try:
            r = requests.get(url, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")
            text = soup.get_text(separator=" ", strip=True)

            pages.append({"url": url, "text": text})
            visited.add(url)

            for link in soup.find_all("a", href=True):
                full_url = urljoin(url, link["href"])
                if urlparse(full_url).netloc == urlparse(BASE_URL).netloc:
                    queue.append(full_url)

        except Exception as e:
            print(f"Failed: {url}", e)

    with open(f"{DATA_DIR}/raw_pages.json", "w") as f:
        json.dump(pages, f, indent=2)

if __name__ == "__main__":
    crawl_website()