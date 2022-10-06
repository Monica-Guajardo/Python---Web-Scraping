from itemloaders.processors import TakeFirst, MapCompose
import scrapy


def remove_whitespace(value):
    return value.strip()

class BookstoreItem(scrapy.Item):
    title = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()
    rating = scrapy.Field()
    stock = scrapy.Field()
    link = scrapy.Field()
    
