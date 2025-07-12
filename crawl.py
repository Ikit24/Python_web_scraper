from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

def normalize_url(url):
    parsed_url = urlparse(url)
    netloc = parsed_url.netloc
    path = parsed_url.path.rstrip('/')
    if not path:
        return netloc
    else:
        return netloc + path

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
