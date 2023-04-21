import subprocess
from flask import flash, redirect, url_for, Blueprint

scrapers = Blueprint('scrapers', __name__)


@scrapers.route('/scraper')
def scrape_data_initiate():
    subprocess.check_output(['scrapy', 'crawl', 'TheDynamicWollplatzSpider'])
    flash(f'Data Scraped Successfully', 'success')
    return redirect(url_for('users.wollplatzScrape'))