from flask import Flask, jsonify
import json
from restaurants import chipotle

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def test():
    menu = chipotle.make_an_order()

    message = 'Hi there, here goes the menu'

    return jsonify({
        'message': message,
        'order': menu
    })
