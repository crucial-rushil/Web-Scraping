# -*- coding: utf-8 -*-
import scrapy
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

class GDP(scrapy.Spider):
    name = 'money' #each spider has a unique name
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['https://worldpopulationreview.com/countries/countries-by-national-debt']

    def parse(self, response):
        countries = response.xpath("//tbody/tr")
        for country in countries:
            name = country.xpath(".//td/a/text()").get() 
            percent = country.xpath(".//td[2]/text()").get()
            yield {
                'country_name': name,
                'gdp_debt': percent
            }
        #in Scrapy, always return data as a dict    
            #absolute_url = f"https://www.worldometers.info{link}"
            #yield response.follow(url=link, callback=self.parse_country, meta={'country_name': name})
 
    #def parse_country(self,response):
        #name = response.request.meta['country_name']
        #rows = response.xpath("(//table[@class='table table-striped table-bordered table-hover table-condensed table-list'])[1]/tbody/tr")
        #for row in rows:
        #    year = row.xpath(".//td[1]/text()").get()
        #    population = row.xpath(".//td[2]/strong/text()").get()
        
        #yield {
        #    'country_name': name,
        #    'year': year,
        #    'population': population
        #}