# Web Crawler with Network Analysis

A comprehensive, production-ready web crawler that provides automated website analysis with multiple output formats including email reports, CSV data exports, and visual network graphs.

## Features

### Core Crawling
- **Asynchronous web crawling** with configurable concurrency
- **Robust error handling** - continues crawling despite individual page failures
- **Configurable limits** - set maximum pages and concurrent connections
- **Internal/External link classification** - distinguishes between site content and external references
- **Professional logging** - detailed error reporting and crawl progress tracking

### Multiple Output Formats
- **Email reports** - automated HTML-formatted reports sent via Gmail
- **CSV data export** - separate files for internal links and external domains
- **Visual network graphs** - PNG visualization showing page connections
- **Console output** - real-time crawl progress and results

### Automation & Scheduling
- **Scheduled crawling** - automated daily/hourly runs with systemd integration
- **Email notifications** - receive reports automatically via email
- **Production deployment** - runs as a background service on Linux/WSL
- **Configurable scheduling** - easily adjust timing for different use cases

### Data Analysis
- **Link relationship mapping** - tracks which pages link to which others
- **Connection strength analysis** - identifies most connected pages
- **External domain tracking** - analyzes external references and dependencies
- **Network visualization** - circular graph layout showing top connected pages

## Installation

### Prerequisites
- Python 3.10+
- uv package manager

### Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Web-Scraper-Python
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```

3. **Configure email settings:**
   ```bash
   mkdir config
   ```
   
   Create `config/mail_config.txt`:
   ```
   email=your.email@gmail.com
   pw=your16characterapppassword
   ```

4. **Set up Gmail App Password:**
   - Enable 2-Step Verification on your Gmail account
   - Go to [myaccount.google.com](https://myaccount.google.com) → Security → App passwords
   - Generate an app password for "Web Crawler"
   - Use the 16-character password in your config file

## Usage

### Direct Crawling
```bash
# Crawl a website with 3 concurrent connections, max 25 pages
uv run main.py https://example.com 3 25
```

### Scheduled Crawling
```bash
# Run automated scheduler (daily at 10:30 AM)
uv run scheduler.py
```

### Production Deployment
```bash
# Set up as systemd service
sudo systemctl enable web-crawler.service
sudo systemctl start web-crawler.service
```

## Output Files

### Email Report
- Formatted text report with internal page counts
- External domain references with frequency
- Sent automatically to configured email address

### CSV Files
- `internal_links.csv` - Internal pages with visit counts
- `external_domains.csv` - External domains with reference counts
- Compatible with Excel, Google Sheets, and data analysis tools

### Network Visualization
- `connections.png` - Visual graph showing page relationships
- Circular layout with top 15 most connected pages
- Black lines indicate link relationships

## Configuration

### Crawler Settings
- `max_concurrency`: Number of simultaneous requests (1-10 recommended)
- `max_pages`: Maximum pages to crawl (prevents infinite crawling)
- `base_url`: Starting URL for the crawl

### Scheduler Settings
- **Schedule**: Modify `@repeat(every().day.at("10:30"))` in `scheduler.py`
- **Check interval**: Adjust `time.sleep(1800)` for different monitoring frequencies

### Email Settings
- **SMTP server**: Uses Gmail's `smtp.gmail.com:587`
- **Authentication**: Requires Gmail app password
- **Format**: Plain text reports with structured data

## Example Output

### Console Output
```
starting crawl: https://news.ycombinator.com/
Visited 1 unique pages so far.
Visited 2 unique pages so far.
...
CSV files internal_links and external_domains generated locally.
Graph visualization created locally and saved as connections.png
```

### Email Report Sample
```
=============================
  REPORT for https://example.com
=============================
Found 25 internal links to https://example.com/articles
Found 15 internal links to https://example.com/about
Found 8 internal links to https://example.com/contact

External Domains:
Referenced github.com 5 times
Referenced twitter.com 3 times
Referenced wikipedia.org 2 times
```

## Error Handling

The crawler includes comprehensive error handling:
- **Network failures** - logged and skipped, crawling continues
- **Malformed HTML** - parsing errors handled gracefully
- **Session timeouts** - automatic retry and continuation
- **Invalid URLs** - filtered out with detailed logging
- **Email failures** - reported but don't stop crawling

## Architecture

- `main.py` - Entry point and argument parsing
- `crawl.py` - Core crawler implementation with AsyncCrawler class
- `scheduler.py` - Automated scheduling and email integration
- `visualizer.py` - Network graph generation with matplotlib
- `config/` - Configuration files (gitignored for security)

## Security

- Email credentials stored in separate config file
- Config files excluded from version control
- App passwords used instead of main Gmail password
- No sensitive data in code repository

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with different websites
5. Submit a pull request

## License

MIT License

Copyright (c) 2025 Attila Szász

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Support

For issues or questions:
- Check the error logs for detailed information
- Verify email configuration for delivery issues
- Test with smaller page limits for large sites
- Review systemd service status for deployment issues
