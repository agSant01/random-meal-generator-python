import random


def many(list_: list):
    qty = random.randint(1, 4)

    items = []
    dummy_list = list_.copy()

    # select qty amount of items without replacement
    while qty > 0:
        choice = random.choice(dummy_list)
        dummy_list.remove(choice)
        items.append(choice)
        qty = qty - 1
    return items


def one(list_: list):
    return random.choice(list_)
