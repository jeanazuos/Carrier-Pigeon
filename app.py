from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from pigeon_news.spiders.News import NewsSpider
from datetime import datetime
import time
import os
import logging
from twisted.internet import reactor

# To be run every time duration in seconds
def sleep(_, duration=int(os.getenv('TIMER'))):
    print(f'sleeping for: {duration}')
    time.sleep(duration)

def crawl(runner):
    d = runner.crawl(NewsSpider)
    d.addBoth(sleep)
    d.addBoth(lambda _: crawl(runner))
    return d

def loop_crawl():
    runner = CrawlerRunner(get_project_settings())
    crawl(runner)
    reactor.run()

if __name__ == '__main__':
    loop_crawl()
