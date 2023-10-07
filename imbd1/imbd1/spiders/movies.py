# -*- coding: utf-8 -*-
"""
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MoviesSpider(CrawlSpider):
    name = 'movies'
    allowed_domains = ['web.archive.org']
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    def start_requests(self):
        yield scrapy.Request(url='http://web.archive.org/web/20200715000935if_/https://www.imdb.com/search/title/?groups=top_250&sort=user_rating', headers={
            'User-Agent': self.user_agent
        })

    #Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True)
    #tells spider to look for links that contain the word 'items' then follow it and extract it and parse reponse through parse_item
    #deny arguement: tells spider NOT to follow link (inverse of allow )
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//h3[@class="lister-item-header"]/a'), callback='parse_item', follow=True, process_request='set_user_agent'),
        
    )
    def set_user_agent(self, request):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        yield
        {
            "title": response.xpath("//div[@class='title_wraper']/h1/text()").get(),
            #"year": response.xpath("//span[@id='titleYear']/a/text()").get(),
            #"duration": response.xpath("(//time)[1]/text()").get(),
            #"genre": response.xpath("//div[@class='subtext']/a/text()").get(),
            #"rating": response.xpath("//span[@itemprop='ratingValue']/text()").get(),
            #"movie_url": response.url,
        }
        #print(response.url) 
"""
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
 
 
class BestMoviesSpider(CrawlSpider):
    name = 'best_movies'
 
    #user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
 
    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?groups=top_250&sort=user_rating', headers={
            #'User-Agent': self.user_agent
        })
 
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"),
             callback='parse_item', follow=True),
        #Rule(LinkExtractor(
        #    restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"))
    )
 
    def parse_item(self, response):
        yield {
            'title': response.xpath("//h1[contains(@class, 'TitleHeader')]/text()").get(),
            'year': response.xpath("//li[@role='presentation']/a/text()").get(),
            'duration': response.xpath("//li[@role='presentation' and position() = 3]/text()").get(),
            'genre': response.xpath("//div[@data-testid='genres']/a/span/text()").get(),
            'rating': response.xpath("//div[contains(@data-testid, 'rating__score')]/span/text()").get(),
            'movie_url': response.url
        }
 