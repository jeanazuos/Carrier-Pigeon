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
        self.collection = mongo_collection_name = os.environ.get('MONGO_COLLECTION')
        self.uri = mongo_uri = os.environ.get('MONGO_URI')
        self.database = mongo_db = os.environ.get('MONGO_DATABASE')
        self.port = mongo_port = int(os.environ.get('MONGO_PORT'))
        self.user = mongo_user = os.environ.get('MONGO_USER')
        self.password = mongo_pass = os.environ.get('MONGO_PASS')
        pass

    #abrir conexao com banco
    def open_spider(self, spider):
        try:
            self.client = MongoClient(
                self.uri,
                self.port,
                username = self.user,
                password = self.password
            )
            self.db = self.client[self.database]
        except Exception as e:
            print(f"Connection mongoDB error {str(e)}")
            return str(e), 400

    def close_spider(self, spider):
        self.client.close()
        pass

    def process_item(self, item, spider):
        self.set_data(item)
        return item

    def set_data(self, item):
        self.db[self.collection].insert(dict(item))