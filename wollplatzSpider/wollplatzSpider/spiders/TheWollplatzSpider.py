import sys
import time

import scrapy
from dotenv import load_dotenv
from scrapy_selenium import SeleniumRequest

# from ..database.connection import db
# from ..database.models import Items, WebsiteUrl
from ..items import WollplatzspiderItem
import os
import pandas as pd
from app import db, app
from wollplatzSpider.database.models import Items, WebsiteUrl, Brands, Selectors
from scrapy.crawler import CrawlerProcess
from scrapy.http import HtmlResponse
from sqlalchemy import create_engine, update
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


load_dotenv()
# driver = webdriver.Chrome()


class ThewollplatzspiderSpider(scrapy.Spider):
    name = 'TheWollplatzSpider'
    start_urls = []
    brand_id, linking_url = [], []

    # def __init__(self):
    #     super().__init__()
    #     self.selectors = None
    #
    # def start_requests(self):
    #     brand_id_counter = 0
    #     website_url = WebsiteUrl.query.all()
    #     for web_url in website_url:
    #         brands_url = Brands.query.filter_by(website_id=web_url.id).all()
    #
    #         for brand_attr in brands_url:
    #             brand = brand_attr.brand_name
    #             product = brand_attr.product_name
    #             # self.brand_id.append(brand_attr.brand_selector)
    #             # self.linking_url.append(brand_attr.linking_url)
    #
    #             url = web_url.links + '/' + web_url.pattern
    #             url = f"{url}".format(i=brand, j=product).replace(' ', '%20')
    #
    #             print('URL :', url)
    #             yield SeleniumRequest(
    #                 url=url,
    #                 wait_time=0,
    #                 wait_until=EC.presence_of_element_located((By.ID, brand_attr.brand_selector)),
    #                 dont_filter=True,
    #                 meta={'linking_url': brand_attr.linking_url}
    #             )
    #         brand_id_counter += 1
    #
    # def parse(self, response, **kwargs):
    #     self.linking_url = response.meta.get('linking_url')
    #
    #     for url in response.xpath(self.linking_url):
    #         selectors = Selectors.query.filter_by(website_id=Brands.query.with_entities(Brands.website_id).filter_by(
    #             linking_url=self.linking_url).first()[0]).first().__dict__
    #         yield response.follow(url.get(), callback=self.parse_products, meta={'selector': selectors})
    #
    # def parse_products(self, response):
    #     print(response)
    #     self.selectors = response.meta.get('selector')
    #     print(self.selectors)
    #     products = {
    #         'title': response.xpath(self.selectors['title_selector']).extract_first(),
    #         'price': response.xpath(self.selectors['price_selector']).extract_first(),
    #         'composition': response.xpath(self.selectors['composition_selector']).extract_first(),
    #         'needle_size': response.xpath(self.selectors['needle_size_selector']).extract_first(),
    #     }
    #
    #     check_product = Items.query.filter_by(title=products['title']).first()
    #     if check_product:
    #         print('----------Data Updated----------')
    #         query = update(Items).where(Items.title == products['title']).values(
    #             price=products['price'], composition=products['composition'], needle_size=products['needle_size'])
    #     else:
    #         print('----------Data Created----------')
    #         query = insert(Items).values(title=products['title'], price=products['price'],
    #                              composition=products['composition'], needle_size=products['needle_size'])
    #     db.session.execute(query)
    #     db.session.commit()


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(ThewollplatzspiderSpider)
    process.start()
