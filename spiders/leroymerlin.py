import scrapy
from scrapy.http import HtmlResponse
from leruapars.items import LeruaparsItem
from scrapy.loader import ItemLoader


class LeroymerlinSpider(scrapy.Spider):
    name = 'leroymerlin'
    allowed_domains = ['leroymerlin.ru']

    def __init__(self, search):
        super(LeroymerlinSpider, self).__init__()
        self.start_urls = [f'https://leroymerlin.ru/search/?q={search}']

    def parse(self, response):

        item_links = response.xpath("//a[@slot='name']")
        for ads in item_links:
            yield response.follow(ads, callback=self.item_parse)

        next_page = response.xpath(
            "//div[@class='next-paginator-button-wrapper']/a/@href").extract_first()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def item_parse(self, response: HtmlResponse):
        loader = ItemLoader(item=LeruaparsItem(), response=response)
        loader.add_xpath('name', "//h1/text()")
        loader.add_xpath('photos',"//img[@slot = 'thumbs']/@src")
        loader.add_value('link',response.url)
        loader.add_xpath('price',"//span[@slot='price']/text()")
        loader.add_xpath('characters',"//dl/div[@class = 'def-list__group']")


        yield loader.load_item()
