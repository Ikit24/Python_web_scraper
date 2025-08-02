import sys, asyncio
from crawl import crawl_site_async
from visualizer import create_graph_visualization
from reporter import print_report

async def main():
    max_concurrency = int(sys.argv[2])
    max_pages = int(sys.argv[3])

    if len(sys.argv) < 4:
        print("usage python main.py <base_url> <max_concurrency> <max_pages>")
        sys.exit(1)

    if len(sys.argv) > 4:
        print("too many arguments provided")
        sys.exit(1)

    if not sys.argv[2].isdigit():
        print("max_concurrency must be an integer")
        sys.exit(1)

    if not sys.argv[3].isdigit():
        print("max_pages must be an integer")
        sys.exit(1)

    print(f"starting crawl: {sys.argv[1]}")

    pages_result, external_domains, page_connections = await crawl_site_async(sys.argv[1], max_concurrency, max_pages)

    for url, count in pages_result.items():
        print(f"{url}: visited {count} times")

    result = print_report(pages_result, sys.argv[1], external_domains)

    create_graph_visualization(page_connections)

    return result

if __name__ == "__main__":
    asyncio.run(main())
