import os
import json
from django.conf import settings
import csv

def find_possible_meals():
    recipie_json_path = os.path.join(settings.BASE_DIR, "data", "recipe_book.json")
    fridge_csv_path = os.path.join(settings.BASE_DIR, "data", "fridge.csv")

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
    fridge_csv_path = os.path.join(settings.BASE_DIR, "data", "fridge.csv")

    with open(fridge_csv_path, "r") as f:
        existing_items = [line.strip() for line in f.readlines()]

    if not remove:
        with open(fridge_csv_path, "a") as f:
            for item in fridge_list:
                if item not in existing_items:
                    f.write(f"{item}\n")
    else:
        with open(fridge_csv_path, "w") as f:
            for item in existing_items:
                if item not in fridge_list:
                    f.write(f"{item}\n")