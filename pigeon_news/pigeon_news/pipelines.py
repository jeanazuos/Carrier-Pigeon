# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pymongo import MongoClient
import os
from datetime import datetime

class PigeonNewsPipeline:

    def mongo_config(self):
        
        self.collection = os.environ.get('MONGO_COLLECTION')
        self.uri = os.environ.get('MONGO_URI')
        self.database = os.environ.get('MONGO_DATABASE')
        self.port = int(os.environ.get('MONGO_PORT'))
        self.user = os.environ.get('MONGO_USER')
        self.password = os.environ.get('MONGO_PASS')

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
        item = cleaner(item)
        self.set_data(item)

    def set_data(self, item):
        self.db[self.collection].insert(dict(item))

# Parser method
def tags_remover(content):
    tags_to_remove = [
    '<title xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/">',
    '</title>',
    '<link xmlns:atom="http://www.w3.org/2005/Atom" xmlns:media="http://search.yahoo.com/mrss/">',
    '</link>'
    ]
    for item_clear in tags_to_remove:
        content = content.split(item_clear)
        if not content[0]:
            content=content[1]
        else:
            content=content[0]
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