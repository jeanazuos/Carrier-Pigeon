from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from pigeon_news.spiders.News import NewsSpider
from datetime import datetime
import schedule
import time
import os
import logging

# Job to be run every x minutes
def job():
    logging.info("Inicio do job { datetime.now().strftime('%m/%d/%Y, %H:%M:%S') }")
    process = CrawlerProcess(get_project_settings())
    process.crawl(NewsSpider)
    process.start()

# Set timer to be run
schedule.every(int(os.getenv('TIMER'))).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)