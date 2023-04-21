import scrapy
from scrapy_selenium import SeleniumRequest

from app import db, app
from wollplatzSpider.database.models import Items, WebsiteUrl, Brands, Selectors
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from scrapy.crawler import CrawlerProcess
from sqlalchemy import insert, update

ctx = app.app_context()
ctx.push()

"""
Create a Global list for selector and append it with brands and product loop and use it wisely.
"""


class ThewollplatzspiderSpider(scrapy.Spider):
    name = 'TheDynamicWollplatzSpider'
    start_urls = []
    brand_id, linking_url = [], []

    def __init__(self):
        super().__init__()
        self.selectors = None

    def start_requests(self):
        website_url = WebsiteUrl.query.all()
        for web_url in website_url:
            brands_url = Brands.query.filter_by(website_id=web_url.id).all()

            for brand_attr in brands_url:
                url = web_url.links + '/' + web_url.pattern
                url = f"{url}".format(i=brand_attr.brand_name, j=brand_attr.product_name).replace(' ', '%20')

                print('URL :', url)
                yield SeleniumRequest(
                    url=url,
                    wait_time=0,
                    wait_until=EC.presence_of_element_located((By.ID, brand_attr.brand_selector)),
                    dont_filter=True,
                    meta={'linking_url': brand_attr.linking_url}
                )

    def parse(self, response, **kwargs):
        self.linking_url = response.meta.get('linking_url')

        for url in response.xpath(self.linking_url):
            selectors = Selectors.query.filter_by(website_id=Brands.query.with_entities(Brands.website_id).filter_by(
                linking_url=self.linking_url).first()[0]).first().__dict__
            yield response.follow(url.get(), callback=self.parse_products, meta={'selector': selectors})

    def parse_products(self, response):
        print(response)
        self.selectors = response.meta.get('selector')
        print(self.selectors)
        products = {
            'title': response.xpath(self.selectors['title_selector']).extract_first(),
            'price': response.xpath(self.selectors['price_selector']).extract_first(),
            'composition': response.xpath(self.selectors['composition_selector']).extract_first(),
            'needle_size': response.xpath(self.selectors['needle_size_selector']).extract_first(),
        }

        check_product = Items.query.filter_by(title=products['title']).first()
        if check_product:
            print('----------Data Updated----------')
            query = update(Items).where(Items.title == products['title']).values(
                price=products['price'], composition=products['composition'], needle_size=products['needle_size'])
        else:
            print('----------Data Created----------')
            query = insert(Items).values(title=products['title'], price=products['price'],
                                         composition=products['composition'], needle_size=products['needle_size'])

        db.session.execute(query)
        db.session.commit()


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(ThewollplatzspiderSpider)
    process.start()
