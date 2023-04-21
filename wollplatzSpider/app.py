import os
import subprocess

from flask import Flask, flash, url_for, redirect, request, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from webapp.forms import WebsiteSelectors

load_dotenv()

db = SQLAlchemy()

app = Flask(__name__)
app.secret_key = 'super secret key'

app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
from wollplatzSpider.database.models import Items, WebsiteUrl, Brands, Selectors
Migrate(app, db)
db.init_app(app)


@app.route('/')
def wollplatzScrape():
    page = request.args.get('page', 1, type=int)
    items = Items.query.order_by(Items.id).paginate(page=page, per_page=5)
    return render_template('index.html', items=items)


@app.route('/scraper')
def scrape_data_initiate():
    subprocess.check_output(['scrapy', 'crawl', 'TheDynamicWollplatzSpider'])
    flash(f'Data Scraped Successfully', 'success')
    return redirect(url_for('wollplatzScrape'))


@app.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    form = WebsiteSelectors()
    if form.validate_on_submit():
        if not WebsiteUrl.query.filter_by(links=form.website_url.data).first():
            website_data = WebsiteUrl(links=form.website_url.data, pattern=form.website_pattern.data)
            db.session.add(website_data)

        web_id = WebsiteUrl.query.with_entities(WebsiteUrl.id).filter_by(links=form.website_url.data).first()

        if not Brands.query.filter_by(product_name=form.product_name.data).first():
            brand_data = Brands(website_id=web_id[0], brand_selector=form.brand_selector_id.data,
                                linking_url=form.linking_url_selector.data, brand_name=form.brand_name.data,
                                product_name=form.product_name.data)
            db.session.add(brand_data)

        if not Selectors.query.filter_by(title_selector=form.title_selector.data).first():
            selector_data = Selectors(website_id=web_id[0], title_selector=form.title_selector.data,
                                      price_selector=form.price_selector.data,
                                      composition_selector=form.composition_selector.data,
                                      needle_size_selector=form.needle_size_selector.data)
            db.session.add(selector_data)
        db.session.commit()

        flash('Website Data has been Added', 'success')
        return redirect(url_for('wollplatzScrape'))
    return render_template('admin_panel.html', title='Admin Panel', form=form, legend='Website Data')


if __name__ == '__main__':
    app.run()