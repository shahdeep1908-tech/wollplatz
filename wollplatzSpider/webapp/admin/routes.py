from flask import flash, url_for, render_template, redirect, Blueprint

from app import db
from webapp.admin.forms import WebsiteSelectors
from wollplatzSpider.database.models import WebsiteUrl, Brands, Selectors


admin = Blueprint('admin', __name__)


@admin.route('/admin', methods=['GET', 'POST'])
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
        return redirect(url_for('users.wollplatzScrape'))
    return render_template('admin_panel.html', title='Admin Panel', form=form, legend='Website Data')