import requests, aiohttp, asyncio
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


def get_urls_from_html(html, base_url, base_domain):
    if not isinstance(html, str):
        raise TypeError("HTML is not a string")

    urls = []
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup.find_all("a"):
        href = tag.get("href")
        if href != None:
            absolute_url = urljoin(base_url, href)
            parsed_url = urlparse(absolute_url)
            netloc = parsed_url.netloc
            if netloc == base_domain:
                urls.append(absolute_url)
    return urls


class AsyncCrawler:
    def __init__(self, base_url, base_domain, max_concurrency):
        self.base_url = base_url
        self.base_domain = base_domain
        self.pages = {}
        self.lock = asyncio.Lock()
        self.max_concurrency = max_concurrency
        self.semaphore = asyncio.Semaphore(max_concurrency)


    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self


    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()


    async def add_page_visit(self, normalized_url):
        async with self.lock:
            if normalized_url in self.pages:
                self.pages[normalized_url] += 1
                return False
            else:
                self.pages[normalized_url] = 1
                return True


    async def get_html(self, url):
        try:
            async with self.session.get(url) as response:
                if response.status_code >= 400:
                    raise Exception(f"HTTP error {response.status}: {response.reason}")

                content_type = response.headers.get('content-type', '')
                if not content_type.startswith('text/html'):
                    raise Exception(f"Content-type is not text/html. Got: {content_type}")
 
                return await response.text()

        except aiohttp.ClientError as e:
            raise Exception(f"Request failed: {str(e)}")


    async def crawl_page(self, url):
        normalized_url = normalize_url(url)
        is_new_page = await self.add_page_visit(normalized_url)
        if not is_new_page:
            return

        async with self.semaphore:
            try:
                HTML = await self.get_html(normalized_url)
            except Exception:
                return
            if HTML is None:
                return
            new_urls = get_urls_from_html(HTML, normalized_url, self.base_domain)

            tasks = []
            for url in new_urls:
                background_task = asyncio.create_task(self.crawl_page(url))
                tasks.append(background_task)
            await asyncio.gather(*tasks)
