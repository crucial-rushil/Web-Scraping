"""
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from read import ReadSpider

process = CrawlerProcess(settings=get_project_settings())
process.crawl(ReadSpider)
process.start()
"""