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
    return f'Welcome to the Chipotle random order generator:<br>\n'\
        'Routes:<br>\n'\
        '\u2022 /restaurant_name/meal | For JSON Response<br>\n' \
        '\u2022 /restaurant_name/meal/txt | For text Response\n'
