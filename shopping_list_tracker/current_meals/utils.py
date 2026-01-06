import os
import json
from django.conf import settings
import csv

def find_possible_meals():
    recipie_json_path = os.path.join(settings.BASE_DIR, "data", "recipe_book.json")
    fridge_csv_path = os.path.join(settings.BASE_DIR, "data", "fridge.txt")

    possible_meals = []

    with open(fridge_csv_path, newline='') as f:
        reader = csv.reader(f)
        available_ingredients = [row[0] for row in reader] 
    with open(recipie_json_path) as f:
        recipe_dictionary = json.load(f)

    for meal, ingredients in recipe_dictionary.items():
        if all(ingredient in available_ingredients for ingredient in ingredients):
            possible_meals.append(meal)

    return possible_meals

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

