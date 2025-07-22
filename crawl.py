import requests, aiohttp, asyncio
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from threading import Thread, Lock


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
    def __init__(self, base_url, base_domain, max_concurrency, max_pages):
        self.base_url = base_url
        self.base_domain = base_domain
        self.pages = {}
        self.lock = asyncio.Lock()
        self.max_concurrency = max_concurrency
        self.semaphore = asyncio.Semaphore(max_concurrency)
        self.max_pages = max_pages
        self.pages_mutex = Lock()
        self.processing_urls = set()


    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self


    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()


    async def add_page_visit(self, normalized_url):
        async with self.lock:
            if normalized_url in self.processing_urls:
                return False
        
        # Add to processing set
            self.processing_urls.add(normalized_url)
            if normalized_url in self.pages:
                self.pages[normalized_url] += 1
                return False
            elif len(self.pages) == self.max_pages:
                return False
            else:
                self.pages[normalized_url] = 1
                print(f"Visited {len(self.pages)} unique pages so far.")
                return True


    async def get_html(self, url):
        try:
            async with self.session.get(url) as response:
                if response.status > 399:
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
            except Exception as e:
                return
            if HTML is None:
                return
            new_urls = get_urls_from_html(HTML, normalized_url, self.base_domain)

            tasks = []
            for url in new_urls:
                with self.pages_mutex:
                    if len(self.pages) >= self.max_pages:
                        break
                background_task = asyncio.create_task(self.crawl_page(url))
                tasks.append(background_task)

            await asyncio.gather(*tasks)


    async def crawl(self):
        await self.crawl_page(self.base_url)
        return self.pages


async def crawl_site_async(base_url, max_concurrency, max_pages):
    parsed_base_domain = urlparse(base_url)
    base_domain = parsed_base_domain.netloc
    async with AsyncCrawler(base_url, base_domain, max_concurrency, max_pages) as crawler:
        pages = await crawler.crawl()
        return pages

def print_report(pages, base_url):
    print(f"""
=============================
  REPORT for {base_url}
=============================
""")

    nr_of_urls = []
    for url, count in pages.items():
        nr_of_urls.append((url, count))
    srtd_lst = sorted(nr_of_urls, key=lambda item: (item[1] * -1, item[0]))

    for url, count in srtd_lst:
        print(f"Found {count} internal links to {url}")
