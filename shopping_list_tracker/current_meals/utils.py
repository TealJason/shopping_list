import os
import json
from django.conf import settings
import csv

def find_possible_meals(available_ingredients):
    recipie_json_path = os.path.join(settings.BASE_DIR, "data", "recipe_book.json")

    # normalize fridge
    available_ingredients = [i.strip().lower() for i in available_ingredients]

    results = []  # list of (meal, missing_list)

    with open(recipie_json_path) as f:
        recipe_dictionary = json.load(f)

    for meal, ingredients in recipe_dictionary.items():
        missing = []

        for ingredient in ingredients:
            ingredient = ingredient.strip().lower()
            if ingredient not in available_ingredients:
                missing.append(ingredient)

        results.append((meal, missing))

    results.sort(key=lambda item: len(item[1]))
    return results

def write_fridge_csv(fridge_list, remove):
    fridge_csv_path = os.path.join(settings.BASE_DIR, "data", "fridge.txt")

    # Normalize input
    fridge_list = [i.strip().lower() for i in fridge_list if i.strip()]

    # Read existing
    if os.path.exists(fridge_csv_path):
        with open(fridge_csv_path, "r") as f:
            existing_items = [line.strip().lower() for line in f]
    else:
        existing_items = []

    if not remove:
        # ADD mode
        merged = set(existing_items)
        merged.update(fridge_list)
    else:
        # REMOVE mode
        merged = set(existing_items) - set(fridge_list)

    # Write back
    with open(fridge_csv_path, "w") as f:
        for item in sorted(merged):
            f.write(item + "\n")

