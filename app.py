from flask import Flask, jsonify, request
import json
from restaurants import chipotle

app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return f'Welcome to the Chipotle random order generator:<br>\n'\
        'Routes:<br>\n'\
        '\u2022 /get-meal | For JSON Response<br>\n' \
        '\u2022 /get-meal/txt | For text Response\n'


@app.route('/get-meal', methods=['GET'])
def get_meal():
    menu = chipotle.make_an_order()

    message = 'Hi there, here goes the menu'

    return jsonify({
        'message': message,
        'order': menu
    })


@app.route('/get-meal/txt', methods=['GET'])
def get_meal_txt():

    agent: str = request.headers.get('User-Agent')

    if agent.startswith('curl'):
        new_line = '\n'
    else:
        new_line = '<br>'

    menu = chipotle.make_an_order()

    menu_as_text = ""

    for m_item in menu:
        val = menu[m_item]

        if isinstance(val, list):
            val = f"[{', '.join(val)}]"

        menu_as_text = f'{menu_as_text}\u2022 {m_item}: {val}{new_line}'

    message = f'Hi there, here goes the menu:{new_line}{menu_as_text}{new_line}'

    return message
