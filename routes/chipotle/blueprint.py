from flask import Blueprint, jsonify, request
from routes.chipotle import dao

bp = Blueprint('chipotle_routes', __name__,
               url_prefix='/chipotle')


@bp.route('/meal', methods=['GET'])
def get_chipotle_meal_json():
    menu = dao.make_an_order()

    message = 'Hi there, here goes the menu'

    return jsonify({
        'message': message,
        'order': menu
    })


@bp.route('/meal/txt', methods=['GET'])
def get_meal_txt():

    agent: str = request.headers.get('User-Agent')

    if agent.startswith('curl'):
        new_line = '\n'
    else:
        new_line = '<br>'

    menu = dao.make_an_order()

    menu_as_text = ""

    for m_item in menu:
        val = menu[m_item]

        if isinstance(val, list):
            val = f"[{', '.join(val)}]"

        menu_as_text = f'{menu_as_text}\u2022 {m_item}: {val}{new_line}'

    message = f'Hi there, here goes the menu:{new_line}{menu_as_text}{new_line}'

    return message
