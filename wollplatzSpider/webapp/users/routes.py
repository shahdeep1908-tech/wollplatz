from flask import request, render_template, Blueprint

from wollplatzSpider.database.models import Items

users = Blueprint('users', __name__)


@users.route('/')
def wollplatzScrape():
    page = request.args.get('page', 1, type=int)
    items = Items.query.order_by(Items.id).paginate(page=page, per_page=5)
    return render_template('index.html', items=items)