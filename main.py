import sys
from crawl import get_html

def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)

    if len(sys.argv) == 2:
        print(f"starting crawl: {sys.argv[1]}")
        try:
            html_content = get_html(sys.argv[1])
            print(html_content)
        except Exception as e:
            print(f"Error fetching HTML: {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
