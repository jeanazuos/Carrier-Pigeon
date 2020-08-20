# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pymongo import MongoClient
import os
from datetime import datetime
import re

class PigeonNewsPipeline:

    def mongo_config(self):
        
        self.collection = os.environ.get('MONGO_COLLECTION')
        self.uri = os.environ.get('MONGODB_HOSTNAME')
        self.database = os.environ.get('MONGODB_DATABASE')
        self.port = int(os.environ.get('MONGO_PORT'))
        self.user = os.environ.get('MONGODB_USERNAME')
        self.password = os.environ.get('MONGODB_PASSWORD')

        self.client = MongoClient(
        self.uri,
        self.port,
        username = self.user,
        password = self.password
        )
        self.db = self.client[self.database]
        
    # Abre conexao com banco
    def open_spider(self, spider):
        self.mongo_config()

    # Fecha conexao com banco
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        # Clean tags
        item = cleaner(item)
        # Check if title exists to don't duplicated
        if not self.get_one_data("title", item['title']):
            self.set_data(item)
        else:
            # implement log
            print("Noticia já existente")

    def set_data(self, item):
        self.db[self.collection].insert(dict(item))

    # it's a find_one() to return a single data
    def get_one_data(self, key, value):
        return self.db[self.collection].find_one({key: value})

# regex to remove html and entities like &lt, &gt, &nbsp
def tags_remover(content):
    cleaner = re.compile('<.*?>|(&.+;)|\s{2,6}')
    content = re.sub(cleaner,'',content)
    return content


# Parser method
def cleaner(item):
    try:
        content = {}
        if item.get('title'):
            title = item.get('title')
            content['title'] = tags_remover(title)

        if item.get('link'):
            link = item.get('link')
            content['link'] = tags_remover(link)
        
        if item.get('description'):
            description = item.get('description')
            content['description'] = tags_remover(description)

        if item.get('publication_date'):
            publication = item.get('publication_date')
            content['publication_date'] = tags_remover(publication)

        if item.get('media'):
            media = item.get('media')
            content['media'] = media

        # Add time now to dict
        content["processing_date"] = processing_date()

        return content
    

    except ValueError:
        #implementar lib de log
        print("Nao foi possivel encontrar a tag title no xml")

def processing_date():
    now = datetime.now()
    today = now.strftime("%d/%m/%Y %H:%M:%S")
    return today

