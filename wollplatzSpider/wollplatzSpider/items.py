# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item


class WollplatzspiderItem(Item):
    # define the fields for your item here like:
    title = Field()
    price = Field()
    composition = Field()
    needle_size = Field()

    links = Field()
    pattern = Field()

    brand_name = Field()
    product_name = Field()

    brand_selector_id = Field()
    specification_selector_id = Field()
    linking_url_selector = Field()
    title_selector = Field()
    price_selector = Field()
    composition_selector = Field()
    needle_size_selector = Field()