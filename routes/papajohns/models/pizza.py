
from utils import one, many
import random

_dough = [
    'Traditional',
    'Thin Crust'
]

_size = [
    'Small',
    'Medium',
    'Large',
    'Xtra Large'
]

_cheeses = [
    'Parmesan Cheese',
    'Romano Cheese',
    'Provolone Cheese',
    'Fontina Cheese',
    'Asiago Cheese',
    'Mozzarella Cheese'
]

_meat_ingredients = [
    'Sausage',  # 0
    'Pepperonni',
    'Chicken',  # 2
    'Bacon',  # 3
    'Ham',
    'Italian Sausage',
    'Beef',  # 6
    'Pork Sausage (Chorizo)',
    'Anchovies'
]

_vegan_ingredients = [
    'Onion',
    'Pineapple',
    'Black Olives',
    'Mushroom',
    'Green Pepper',
    'Tomato',
]

_base_sauces = [
    'Tomato Sauce',
    'Alfredo Sauce'
]

_additional_toppings = [
    'Sazonador Italiano',
    'BBQ Sauce',
    'Garlic Sauce',
    'Alfredo Sauce with Spinach'
]

_signature_pizzas = [
    # Salchicha, Pepperoni, Mezcla de 6 Quesos (Parmesano, Romano, Provolone, Fontina, Asiago y Mozzarella) y Sazonador Italiano.
    {'name': "John's Favorite", 'ingredients': [
        _meat_ingredients[0], _meat_ingredients[1], f"6 cheeses ({', '.join(_cheeses[0:5])})"]},
    # Pollo, Tocino, Cebolla, Piña, Salsa BBQ como base y Queso Mozzarella.
    {'name': "Hawaiian Chicken BBQ", 'ingredients': [
        _meat_ingredients[2], _meat_ingredients[3], _vegan_ingredients[0], _vegan_ingredients[1], f'{_additional_toppings[1]} as base sauce', _cheeses[5]]},
    # Pollo, Jamon, Cebolla, Salsa BBQ como base.
    {'name': "Chicken BBQ", 'ingredients': [
        _meat_ingredients[2], _meat_ingredients[4], _vegan_ingredients[0], f'{_additional_toppings[1]} as base sauce']},
    # Pepperoni, Salchicha Italiana, Jamón, Champiñón Fresco, Cebolla, Pimiento Verde, Aceitunas Negras.
    {'name': "The Works", 'ingredients': [
        _meat_ingredients[1], _meat_ingredients[4], _meat_ingredients[5], *_vegan_ingredients[2:5]]},
    # Pepperoni, Jamón, Salchicha, Tocino, Carne de Res.
    {'name': "All The Meats", 'ingredients': [
        _meat_ingredients[1], _meat_ingredients[4], _meat_ingredients[0], _meat_ingredients[3], _meat_ingredients[6]]},
    # Pepperoni, Jamón, Salchicha Italiana, Cebolla y Pimientos Verdes.
    {'name': "New York", 'ingredients': [
        _meat_ingredients[1], _meat_ingredients[4], _meat_ingredients[5], _vegan_ingredients[0], _vegan_ingredients[4]]},
]

_specialty_pizzas = [
    # Mezcla de 6 Quesos (Parmesano, Romano, Provolone, Fontina, Asiago y Mozzarella) y Sazonador Italiano
    {'name': "Six Cheese", 'ingredients': [
        f"6 cheeses ({', '.join(_cheeses[0:5])})", _additional_toppings[0]]},
    {'name': "Garden Fresh", 'ingredients': [
        _vegan_ingredients[0], *_vegan_ingredients[2:7]]},
    {'name': "Hawaiana", 'ingredients': [
             _vegan_ingredients[1], _meat_ingredients[4], f'{_base_sauces[0]} as base sauce']},
    # Salsa Alfredo con Espinaca como base y Queso Mozzarella
    {'name': "Spinach Alfredo", 'ingredients': [
        f'{_additional_toppings[3]} as base sauce', _cheeses[5]]},
    # Pollo, Jamón, Tocineta, y Salsa de Ajó
    {'name': "Puertorriqueña", 'ingredients': [
        *_meat_ingredients[2:5], _additional_toppings[2]]},
    # Pollo, tocino, jamón, tomates.
    {'name': "Chicken Club", 'ingredients': [
        *_meat_ingredients[2:5], _vegan_ingredients[5]]},
]


def _is_vegan(ingredients):
    _meat_ingredients_set = set(_meat_ingredients)
    return _meat_ingredients_set.isdisjoint(ingredients)


def _random_pizza(**kwargs):
    vegan = kwargs.get('vegan', False)

    ingredients = set()
    was_vegan = False
    if random.random() > 0.5:
        # get vegies
        veggies = many(_vegan_ingredients, min_=0, max_=3)
        was_vegan = True
        ingredients = ingredients.union(veggies)

    if (random.random() > 0.5 or not was_vegan) and not vegan:
        min_ = 2 if not was_vegan else 1
        meats = many(_meat_ingredients, min_=min_, max_=3)
        ingredients = ingredients.union(meats)

    if len(ingredients) == 0:
        ingredients.add('Cheese')

    return {
        'name': 'Chef Creation',
        'ingredients': list(ingredients),
        'base_sauce': one(_base_sauces)
    }


def _get_pizzas(pizza_list, **kwargs):
    vegan = kwargs.get('vegan', False)

    pizza = random.choice(pizza_list)
    if vegan:
        vegan_pizzas = list(filter(
            lambda list_item: _is_vegan(list_item.get('ingredients', [])),
            pizza_list
        ))
        print(f'jhv  {vegan_pizzas}')
        pizza = random.choice(vegan_pizzas)

    pizza.update({'base_sauce': one(_base_sauces)})
    return pizza


def _add_restaurant_label(dict_: dict):
    new_dict = ({'restaurant': "Papa Juan", 'order': dict_})
    return new_dict


_types = {
    'specialty': lambda vegan: _get_pizzas(_specialty_pizzas, vegan=vegan),
    'signature': lambda vegan: _get_pizzas(_signature_pizzas if not vegan else _specialty_pizzas, vegan=vegan),
    'random': _random_pizza
}


def get_regular(json=True):
    response = None
    if random.random() > 0.5:
        # get whole pizza
        desicion = random.choice(list(_types))
        response = _add_restaurant_label({
            'pizza': _types[desicion](vegan=False)
        })
    else:
        # get half & half
        halfs = random.sample(list(_types), 2)
        response = _add_restaurant_label({
            'pizza': {
                'first_half': _types[halfs[0]](vegan=False),
                'second_half': _types[halfs[1]](vegan=False)
            }
        })

    return response


def get_vegan(json=True):
    response = None
    if random.random() > 0.5:
        # get whole pizza
        desicion = random.choice(list(_types))
        response = _add_restaurant_label(
            {'pizza': _types[desicion](vegan=True)})
    else:
        # get half & half
        halfs = random.sample(list(_types), 2)
        response = _add_restaurant_label({
            'pizza': {
                'first_half': _types[halfs[0]](vegan=True),
                'second_half': _types[halfs[1]](vegan=True)
            }
        })

    return response


if __name__ == "__main__":
    for val_ in _signature_pizzas:
        print(val_)

    for val_ in _specialty_pizzas:
        print(val_)
    print(f'Rand pizza:\n{_random_pizza()}')
