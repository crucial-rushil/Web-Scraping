# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//article[@class='product_pod']/div/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//li[@class='next']/a"))
    )

    def parse_item(self, response):
        yield {
            'title': response.xpath("//div[@class='col-sm-6 product_main']/h1/text()").get(),
            'price': response.xpath("//div[@class='col-sm-6 product_main']/p[@class='price_color']/text()").get(),
        }
"""
Notes on the Rule Object:
    -> The first arguement in the Rule LinkExtractor object is the restrict_xpaths which dictate what links the spider can go to
    -> this arguement MUST BE A LINK
    -> then the callback functions basically states what function its gonna run
    -> make sure when selecting elements from the callback function do so from the page of link you send the robot to not like the 
    basic ass preview page
    -> p kewl
"""