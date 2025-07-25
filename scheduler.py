from schedule import every, repeat, run_pending
from main import main
import time
import asyncio
import sys

@repeat(every().day.at("10:30"))
def scheduler():
    sys.argv = ["main.py", "https://news.ycombinator.com/", "3", "25"]
    asyncio.run(main())

while True:
    run_pending()
    time.sleep(1800)
