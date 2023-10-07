# -*- coding: utf-8 -*-
import scrapy
from scrapy.shell import inspect_response
import logging

#NOTES:
#you can have multiple spiders but each spider must have a unique name
#allowed domains list: must contain all the domain names the spider is allowed to access & scrape
#ex: if website contains links whose domain names r diff than the allowed_domains, then it will not be
#scraped. 
#in allowed domains list NEVER EVER put the HTTP protocol in the beginning of the list
#start_urls: tells scrapy what to scrape. Make sure to add 's' depending on website's protocol
#parse method: parse the response we get back from the spider

#to run this file in the terminal from VS Code do the following steps.
#1. Go to View and open a new terminal
#2. Type the command: conda activate virtual2 (virtual2 is the name of the workspace I am using right now)
#3. Then type the command: scrapy crawl countries (this will return a dict of all the countries)

#Filtered offsite request: means to delete extra forward slash in allowed_domains list

'''
Detailed Notes about this Program:

--> The Scraping Cycle:
    - Start by generating initial requests to crawl the first URL's and then specify a callback function to be called with the response downloaded
    from these requests
    - in the call back function you parse the web page and return item objects
    - parse the page contents using Selectors
    - return the items to a database
--> Parse method:
    - The parse method is in charge of processing the response and returning scraped data and more URLS to follow
    - in this case the parse method first gets a list of all countries
    - then it stores the list name and list link in two variables
    - then the function passes these arguements to another function that scrapes more info abt the country in particular
    - response.follow(url, callback)
    - the function above will load the next page and call the next function for scrapy to execute to scrape its contents.
    - request.meta --> it will allow you to move data between two functions
    response.follow and Scrapy.request are the same thing btw
'''


class CountriesSpider(scrapy.Spider):
    name = 'countries' #each spider has a unique name
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/world-population/population-by-country/']

    def parse(self, response):
        countries = response.xpath("//td/a")
        for country in countries:
            name = country.xpath(".//text()").get() 
            link = country.xpath(".//@href").get()

        #in Scrapy, always return data as a dict    
            #absolute_url = f"https://www.worldometers.info{link}"
            yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})
 
    def parse_country(self,response):
        name = response.request.meta['country_name']
        rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()
        
            yield {
                'country_name': name,
                'year': year,
                'population': population
            }