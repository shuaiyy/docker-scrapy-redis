# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from ..items import  Moko1Item
from scrapy_redis.spiders import RedisCrawlSpider



class MokoSpiderSpider(RedisCrawlSpider):
    name = 'moko_spider'
    allowed_domains = ['moko.cc']
    # start_urls = ['http://www.moko.cc/moko/post/1.html']
    redis_key = 'moko_spider:start_urls'


    rules = (
        # http://www.moko.cc/moko/post/1.html
        Rule(LinkExtractor(allow=r'http://www\.moko\.cc/moko/post/\d+\.html'), follow=True),
        # http://www.moko.cc/post/1227771.html
        Rule(LinkExtractor(allow=r'http://www\.moko\.cc/post/\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = Moko1Item()
        item['name'] = response.css("#workNickName::text").extract()[0]
        item['index_url'] = response.css("div.info h2.website::text").extract()[0]
        # item['work'] = response.css("")
        # item['location'] = response.css("")
        item['pic_urls'] = response.css("div.pic.dBd  p.picBox  img::attr(src2)").extract()

        return item
