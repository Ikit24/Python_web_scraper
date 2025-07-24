# Web Crawler Link Counter

A Python-based web crawler that analyzes websites and counts both internal and external links for each page. It generates structured reports summarizing the findings, making it easy to visualize the linking structure of any website.

## Features

- **Recursive crawling** - Systematically explores websites starting from a user-defined URL
- **Link analysis** - Counts and categorizes internal vs external links for each page
- **Duplicate handling** - Skips already-visited pages to avoid infinite loops
- **Error resilience** - Gracefully handles broken links and unreachable URLs
- **Summary reporting** - Outputs comprehensive reports to console or file
- **Configurable limits** - Control crawling depth and page limits

## Demo Output

```console
Crawling: https://example.com

Page: https://example.com/
  Internal Links: 15
  External Links: 3

Page: https://example.com/about
  Internal Links: 7
  External Links: 1

Page: https://example.com/contact
  Internal Links: 2
  External Links: 0

--- SUMMARY ---
Total Pages Crawled: 3
Total Internal Links: 24
Total External Links: 4
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/web-crawler-link-counter.git
cd web-crawler-link-counter
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

Run the crawler with a starting URL:

```bash
python crawler.py https://example.com
```

### Advanced Options

```bash
# Limit the number of pages to crawl
python crawler.py https://example.com --max-pages 50

# Save output to a file
python crawler.py https://example.com --output report.txt
```

### Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--max-pages N` | Limit the number of pages to crawl | 100 |
| `--output FILE` | Save the summary to a file instead of printing | Console output |

## Requirements

- **Python**: 3.9 or higher
- **Dependencies**:
  - `requests` - HTTP library for web requests
  - `beautifulsoup4` - HTML parsing library

Install all dependencies:
```bash
pip install requests beautifulsoup4
```

## Project Structure

```
web-crawler-link-counter/
├── crawler.py          # Main crawler script
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── examples/          # Example outputs and usage
```

## Extending the Project

Here are some ideas for extending functionality:

- **Export formats** - Save reports as CSV, JSON, or XML for further analysis
- **Visualization** - Create link graphs using `networkx` or `matplotlib`
- **Scheduling** - Automate crawler runs and email reports periodically
- **Advanced filtering** - Add URL pattern matching and content type filtering
- **Performance** - Implement concurrent crawling for faster processing
- **Testing** - Add comprehensive unit and integration tests

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows Python best practices and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

### v1.0.0
- Initial release with basic crawling functionality
- Console output support
- Error handling for broken links


**Note**: Always respect websites' `robots.txt` files and crawling policies. Use responsibly and avoid overwhelming servers with too many concurrent requests.
