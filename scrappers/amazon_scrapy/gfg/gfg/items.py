# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class GfgItem(Item):
    product_name = Field()
    product_sale_price = Field()
    product_availability = Field()
