# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os
from urllib.parse import urlparse

class LeruaparsImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    print(img)
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):
        if results:
            item['photos'] = [itm[1] for itm in results if itm[0]]
        return item


    def file_path(self, request, response=None, info=None, *, item=None):
        return item['name']+'/'+ os.path.basename(urlparse(request.url).path)

class LeruaparsPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.lerua


    def process_item(self, item, spider):

        collection = self.mongo_base[spider.name]
        collection.insert_one(item)

        return item
