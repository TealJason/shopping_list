import os
import json
from django.conf import settings

def create_shopping_list(selected_meals, ommit):
    recipe_path = os.path.join(settings.BASE_DIR, "data", "recipe_book.json")
    fridge_path = os.path.join(settings.BASE_DIR, "data", "fridge.txt")
    
    required_ingredients = {}
    if not ommit:
        if os.path.exists(fridge_path):
            with open(fridge_path) as f:
                fridge_contents = [line.strip().lower() for line in f]
        else:
            fridge_contents = []
    else:
        fridge_contents = []
        
    with open(recipe_path) as f:
        recipe_dictionary = json.load(f)

    for meal in selected_meals:
        ingredients = recipe_dictionary.get(meal, [])

        for ingredient in ingredients:
            ingredient = ingredient.strip().lower()

            if ingredient in fridge_contents:
                continue

            if ingredient in required_ingredients:
                required_ingredients[ingredient] += 1
            else:
                required_ingredients[ingredient] = 1

    return required_ingredients