from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from app import db


class WebsiteUrl(db.Model):
    """
    Defines the items model
    """
    __tablename__ = "website_url"

    id = db.Column("id", db.Integer, primary_key=True)
    links = db.Column("links", db.String)
    pattern = db.Column("pattern", db.String)


class Brands(db.Model):
    """
    Defines the items model
    """

    __tablename__ = "brands"

    id = db.Column("id", db.Integer, primary_key=True, index=True)
    website_id = db.Column("website_id", db.Integer, ForeignKey('website_url.id'))
    website_url = relationship('WebsiteUrl', backref=backref('website_url', uselist=False))

    brand_selector = db.Column("brand_selector", db.String)
    linking_url = db.Column("linking_url", db.String)
    brand_name = db.Column("brand_name", db.String)
    product_name = db.Column("product_name", db.String)


class Items(db.Model):
    """
    Defines the items model
    """

    __tablename__ = "items"

    id = db.Column("id", db.Integer, primary_key=True, index=True)
    title = db.Column("title", db.String)
    price = db.Column("price", db.String)
    composition = db.Column("composition", db.String)
    needle_size = db.Column("needle_size", db.String)


class Selectors(db.Model):
    """
    Defines the items model
    """
    __tablename__ = "selectors"

    id = db.Column("id", db.Integer, primary_key=True, index=True)
    website_id = db.Column("website_id", db.Integer, ForeignKey('website_url.id'))
    website_url = relationship('WebsiteUrl', backref=backref('web_id', uselist=False))

    title_selector = db.Column("title_selector", db.String)
    price_selector = db.Column("price_selector", db.String)
    composition_selector = db.Column("composition_selector", db.String)
    needle_size_selector = db.Column("needle_size_selector", db.String)
