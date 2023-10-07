# -*- coding: utf-8 -*-
import scrapy


class SimpleSpider(scrapy.Spider):
    name = 'simple'
    allowed_domains = ['www.scrapebay.com']
    start_urls = ['https://www.scrapebay.com/ebooks']

    def parse(self, response):
        for book in response.css('.col'):
            title = book.css('h5 ::text').get() 
            link = response.urljoin(
                book.css('a.pdf ::attr(href)').get()
                ) 

            yield
            {
                'Title':title,
                'file_urls':[link]
            }
