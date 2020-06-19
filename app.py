from flask import Flask, jsonify, request
import json

from routes.chipotle import blueprint as chipotle_bp
from routes.papajohns import blueprint as papajohns_bp

app = Flask(__name__)

app.register_blueprint(chipotle_bp.bp)
app.register_blueprint(papajohns_bp.bp)
app.config['JSON_SORT_KEYS'] = False


@app.route('/', methods=['GET'])
def welcome():
    agent: str = request.headers.get('User-Agent')

    new_line = '<br>'
    if agent.startswith('curl'):
        new_line = '\n'

    return f'Welcome to the Chipotle random order generator:{new_line}'\
        f'Routes:{new_line}'\
        f'\u2022 /chipotle/meal | For JSON Response{new_line}' \
        f'\u2022 /chipotle/meal/txt | For TEXT Response{new_line}' \
        f'\u2022 /papajuan | To see the diferent available random menu option{new_line}'
