import scrapy
import unicodedata

from bookstore.items import BookstoreItem

class BookySpider(scrapy.Spider):
    name = 'booky'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/index.html']

    def parse(self, response):
        pass
