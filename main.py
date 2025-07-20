import sys, asyncio
from crawl import crawl_site_async

async def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)

    print(f"starting crawl: {sys.argv[1]}")
    pages_result = await crawl_site_async(sys.argv[1])
    print(pages_result)

if __name__ == "__main__":
    asyncio.run(main())
