import scrapy

class BookstoreItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    stock = scrapy.Field()
    link = scrapy.Field()
    
