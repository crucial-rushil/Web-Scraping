# -*- coding: utf-8 -*-
import scrapy


class SpecialOffersSpider(scrapy.Spider):
    name = 'special_offers'
    allowed_domains = ['web.archive.org']
    #start_urls = ['https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html']
    # we dont need it because we defined the start url in the start requests method so ye

    def start_requests(self):
        yield scrapy.Request(url="https://web.archive.org/web/20190225123327/https://www.tinydeal.com/specials.html", callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
        })

    def parse(self, response):
        targets = response.xpath("//ul[@class='productlisting-ul']/div/li")
        for product in targets:
            yield {
                'title': product.xpath(".//a[@class='p_box_title']/text()").get(),
                'url': response.urljoin(product.xpath(".//a[@class='p_box_title']/@href").get()),
                'discoutned_price': product.xpath(".//div[@class='p_box_price']/span[1]/text()").get(),
                'original_price': product.xpath(".//div[@class='p_box_price']/span[2]/text()").get(),
                'User-Agent': response.request.headers["User-Agent"]
            }
        next_page = response.xpath("//a[@class='nextPage']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
            })
