from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from leruapars.spiders.leroymerlin import LeroymerlinSpider
from leruapars import settings

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)

    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(LeroymerlinSpider, search = 'ковер детский')


    process.start()