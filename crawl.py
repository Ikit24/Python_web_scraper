from urllib.parse import urlparse

def normalize_url(url):
    parsed_url = urlparse(url)
    netloc = parsed_url.netloc
    path = parsed_url.path.rstrip('/')
    if not path:
        return netloc
    else:
        return netloc + path

def get_urls_from_html(html, base_url):
    pass
