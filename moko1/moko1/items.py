# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Moko1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    index_url = scrapy.Field()
    location = scrapy.Field()
    work = scrapy.Field()
    pic_urls = scrapy.Field()
