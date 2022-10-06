
import scrapy


class BookstoreItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    rating = scrapy.Field()
    link = scrapy.Field()
    
