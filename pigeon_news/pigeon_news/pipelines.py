# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
from pymongo import MongoClient
import os

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
        self.set_data(item)

    def set_data(self, item):
        self.db[self.collection].insert(dict(item))
