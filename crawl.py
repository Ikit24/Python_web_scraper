import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


def normalize_url(url):
    parsed_url = urlparse(url)
    netloc = parsed_url.netloc
    path = parsed_url.path.rstrip('/')
    if not path:
        return parsed_url.scheme + "://" + netloc
    else:
        return parsed_url.scheme + "://" + netloc + path


def get_urls_from_html(html, base_url):
    if not isinstance(html, str):
        raise TypeError("HTML is not a string")

    urls = []
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all("a"):
        href = tag.get("href")
        if href != None:
            absolute_url = urljoin(base_url, href)
            urls.append(absolute_url)
    return urls


def get_html(url):
    try:
        r = requests.get(url)

        if r.status_code >= 400:
            raise Exception(f"HTTP error {r.status_code}: {r.reason}")

        content_type = r.headers.get('content-type', '')
        if not content_type.startswith('text/html'):
            raise Exception(f"Content-type is not text/html. Got: {content_type}")
 
        return r.text

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {str(e)}")

def crawl_page(base_url, current_url=None, pages=None):
    if pages is None:
        pages = {}

    if current_url is None:
        current_url = base_url
    parsed1 = urlparse(current_url)
    parsed2 = urlparse(base_url)
    if not parsed1.netloc == parsed2.netloc:
        return

    current_url = normalize_url(current_url)

    if current_url in pages:
        pages[current_url] += 1
        return
    else:
        pages[current_url] = 1

    print(f"Crawling: {current_url}")
    try:
        HTML = get_html(current_url)
    except Exception:
        return
    if HTML is None:
        return
    URL = get_urls_from_html(HTML, base_url)

    for url in URL:
        crawl_page(base_url, url, pages)

    return pages
