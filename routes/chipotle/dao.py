import random
from utils import many, one

_style = ['Burrito', 'Bowl']

_protein = [
    'Chicken, single',
    'Steak, single',
    'Carnitas, single',
    'Barbacoa, single',
    'Sofritas, single',
    'Chicken, double',
    'Steak, double',
    'Carnitas, double',
    'Barbacoa, double',
    'Sofritas, double'
]

_beans = ['Pinto', 'Black']

_rice = ['White', 'Brown']

_topping = [
    'Mild',
    'Medium',
    'Hot',
    'Sour Cream',
    'Corn',
    'Cheese',
    'Guacamole',
    'Lettuce'
]


def _veggies():
    need_veggies = random.random() > 0.5

    if need_veggies:
        return 'Get Veggies today'

    return "Don't get veggies today"


def _chips():
    should_get = random.random() > 0.5
    if should_get:
        return 'You should get chips today'
    return "Emm, don't get chips today"


def _tortilla():
    should_get = random.random() > 0.5
    if should_get:
        return 'You should get tortilla today'
    return "Emm, don't get tortilla today"


def make_an_order() -> dict:
    return {
        'Style': one(_style),
        'Rice': one(_rice),
        'Beans': one(_beans),
        'Protein': one(_protein),
        'Veggies': _veggies(),
        'Toppings': many(_topping),
        'Chips': _chips(),
        'Side Tortilla': _tortilla()
    }


if __name__ == "__main__":
    print(make_an_order())
