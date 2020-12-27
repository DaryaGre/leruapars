# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose, TakeFirst
import re

def process_photos(photo):
    try:
        photo = photo.replace('/f_auto,q_90,w_82,h_82,c_pad,b_white,d_photoiscoming.png/','/')
        return photo
    except:
        return photo

def process_price(price):
    try:
        price=int(re.sub(r'[^0-9]+','',price))
        return price
    except:
        return price

def process_characters(characters):
    characters = characters.replace('<div class="def-list__group">\n'
                '            <dt class="def-list__term">','')

    characters = characters.replace('</dt>\n'
                '            <dd class="def-list__definition">\n'
                '                ', ':')

    characters = characters.replace('\n'
                '                \n'
                '            </dd>\n'
                '        </div>', '')

    return characters


class LeruaparsItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field(output_processor = TakeFirst())
    photos = scrapy.Field(input_processor = MapCompose(process_photos))
    link = scrapy.Field(output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(process_price),output_processor = TakeFirst())
    characters = scrapy.Field(input_processor = MapCompose(process_characters))
    _id = scrapy.Field()
