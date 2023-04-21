from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class WebsiteSelectors(FlaskForm):
    website_url = StringField('Website Url', validators = [DataRequired()])
    website_pattern = StringField('Website Pattern', validators = [DataRequired()])

    brand_selector_id = StringField('Brand Selector ID', validators = [DataRequired()])
    linking_url_selector = StringField('Linking Url Selector Path', validators=[DataRequired()])
    brand_name = StringField('Brand Name', validators=[DataRequired()])
    product_name = StringField('Product Name', validators=[DataRequired()])

    title_selector = StringField('Title Selector Path', validators = [DataRequired()])
    price_selector = StringField('Price Selector Path', validators = [DataRequired()])
    composition_selector = StringField('Composition Selector Path', validators = [DataRequired()])
    needle_size_selector = StringField('Needle-Size Selector Path', validators = [DataRequired()])

    submit = SubmitField('Add Data')
