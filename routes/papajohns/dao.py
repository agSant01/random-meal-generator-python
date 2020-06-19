from routes.papajohns.models import pizza
import random

_food_type = [pizza]


def make_order() -> dict:
    selected_food_type = random.choice(_food_type)
    return selected_food_type.get_regular()


def make_vegan_order() -> dict:
    selected_food_type = random.choice(_food_type)
    return selected_food_type.get_vegan()
