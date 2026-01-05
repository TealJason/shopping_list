import os
import json
from django.conf import settings

def create_shopping_list(selected_meals):
    path = os.path.join(settings.BASE_DIR, "data", "recipe_book.json")

    required_ingredients = {}

    with open(path) as f:
        recipe_dictionary = json.load(f)

    for meal in selected_meals:
        ingredients = recipe_dictionary.get(meal, [])

        for ingredient in ingredients:
            if ingredient in required_ingredients:
                required_ingredients[ingredient] += 1
            else:
                required_ingredients[ingredient] = 1

    return required_ingredients
