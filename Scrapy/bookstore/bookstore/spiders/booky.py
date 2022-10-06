import scrapy
import unicodedata

from bookstore.items import BookstoreItem

class BookySpider(scrapy.Spider):
    name = 'booky'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/index.html']

    def parse(self, response):
        items = BookstoreItem()
        titles = response.css("h3 a::text").extract()
        ratings = response.xpath("//article/p/@class").extract()
        stocks = response.xpath('//div/p[@class="instock availability"]/text()').extract()
        links = response.xpath('//h3/a/@href').extract()
        
        
        
    
        
        item['title'] = title
        item['rating'] = rating
        item['price'] = price
        item['stock'] = stock
        item['link'] = link
        
        
        
