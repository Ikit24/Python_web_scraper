import sys
from crawl import get_html, crawl_page

def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)

    print(f"starting crawl: {sys.argv[1]}")
    pages_result = crawl_page(sys.argv[1])
    print(pages_result)

if __name__ == "__main__":
    main()
