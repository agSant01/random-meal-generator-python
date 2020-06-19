from flask import Blueprint, request, jsonify
from routes.papajohns import dao
from utils import format_response

bp = Blueprint('papajohns', __name__,  url_prefix='/papajohn')


@bp.route('/meal')
def regular_meal():
    data = dao.make_order()
    return format_response(data, request)


@bp.route('/meal/vegan')
def vegan_meal():
    data = dao.make_vegan_order()
    return format_response(data, request)


@bp.route('/pizza')
def pizza():
    data = dao.pizza.get_regular()
    return format_response(data, request)


@bp.route('/pizza/vegan')
def pizza_vegan_meal():
    data = dao.pizza.get_vegan()
    return format_response(data, request)
