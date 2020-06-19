from flask import Blueprint, request, jsonify
from routes.papajohns import dao
from utils import format_response

bp = Blueprint('papajohns', __name__,  url_prefix='/papajuan')


@bp.route('/', methods=['GET'])
def papajuan():
    agent: str = request.headers.get('User-Agent')

    new_line = '<br>'
    if agent.startswith('curl'):
        new_line = '\n'

    return f"This is Papa Juan's Random meal store. You can select from the following to satisfy your random needs:{new_line*2}"\
        f'\u2022 /papajuan/meal | For a completly random meal{new_line}' \
        f'\u2022 /papajuan/meal/vegan | For a completly random and vegan meal{new_line}' \
        f'\u2022 /papajuan/pizza | For a random pizza{new_line}' \
        f'\u2022 /papajuan/pizza/vegan | For a completly random vegan pizza{new_line*2}' \
        f'All these routes accept the argument output to select a JSON or TEXT outputs.{new_line}' \
        f'Those are the only two supported response formats.{new_line*2}' \
        f'Example: /papajuan/meal/vegan?output=text{new_line}' \



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
