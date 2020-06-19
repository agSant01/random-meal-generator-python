import random
from flask import jsonify


def many(list_: list, min_=1, max_=4):
    qty = random.randint(min_, max_)
    dummy_list = list_.copy()
    return random.sample(list_, qty)


def one(list_: list):
    return random.choice(list_)


def dict_to_text(dict_: dict, new_line: str) -> str:
    order = dict_.get('order', None)

    tab = '  '
    if new_line == '<br>':
        tab = '&nbsp;&nbsp;&nbsp;'

    if order is None:
        return 'An error happened'

    text = f"{tab}Feeling adventurous? This is what I found for {dict_.get('restaurant', '--Unavailable--')}{new_line}"\
        f"{tab}Yeah, I can't use that name, but you know what I mean ;){new_line}{new_line}"
    text += _get_recursive("", new_line, tab, order)

    return text


def _get_recursive(text_, new_line, tab, dict_: dict):
    for m_item in dict_:
        val = dict_[m_item]
        if isinstance(val, dict):
            text_ += tab + m_item.title() + ':' + new_line
            text_ += _get_recursive("", new_line, f'{tab}{tab}', val)
        elif isinstance(val, list):
            val = f"{', '.join(val)}"
            text_ += f"{tab}\u2022 {m_item.title().replace('_', ' ')}: {val.replace('_', ' ')}{new_line}"
        else:
            text_ += f"{tab}\u2022 {m_item.title().replace('_', ' ')}: {val.replace('_', ' ')}{new_line}"

    return text_


def format_response(data, request):
    output_type = request.args.get('output', 'json')
    agent: str = request.headers.get('User-Agent')

    new_line = '<br>'
    if agent.startswith('curl'):
        new_line = '\n'

    if output_type == 'json':
        return jsonify(data)
    elif output_type == 'text':
        return dict_to_text(data, new_line)
    else:
        # fallback to json
        return jsonify(data)
