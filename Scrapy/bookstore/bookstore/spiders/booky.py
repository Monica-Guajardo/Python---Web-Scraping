import scrapy
import unicodedata

from bookstore.items import BookstoreItem

class BookySpider(scrapy.Spider):
    name = 'booky'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/index.html']

    def parse(self, response):
        items = BookstoreItem()
        titles = response.xpath('//h3/a/text()').extract()
        ratings = response.xpath("//article/p/@class").extract()
        price = response.xpath('//div/p[@class="price_color"]/text()').extract()
        stocks = response.xpath('//div/p[@class="instock availability"]/text()').extract()
        links = response.xpath('//h3/a/@href').extract()
        
        #Transform ratings and links
        ratings = [rating.replace("star-rating","") for rating in ratings]
        links = [f"http://books.toscrape.com/{link}" for link in links] 
        
        zip_info = zip(titles, ratings, price, stocks, links)
        info_list = list(zip_info)
        
        for row in info_list:
            title, rating, price, stock, link = row
            items['title'] = title
            items['rating'] = rating
            items['price'] = str(price)
            items['stock'] = stock
            items['link'] = link
            
            yield items
        
        jump_page = response.css('.next a').attrib['href']
        if jump_page is not None:
            yield response.follow(jump_page, callback = self.parse)
        
