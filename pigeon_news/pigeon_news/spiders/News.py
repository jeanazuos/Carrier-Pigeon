# -*- coding: utf-8 -*-
import scrapy
from pigeon_news.items import PigeonNewsItem

class NewsSpider(scrapy.Spider):
    name = 'News'
    allowed_domains = ['valorinveste.globo.com']
    start_urls = ['http://valorinveste.globo.com/rss/valorinveste/ultimas-noticias']

    def parse(self, response):
        for article in response.css("item"):
            title = article.css("title").extract_first()
            url = article.css("link").extract_first()
            description = article.css("description").extract_first()
            media = article.css("media\\:content::attr(url)").extract_first()

            notice = PigeonNewsItem(title=title, link=url, description=description, media=media)
            yield notice