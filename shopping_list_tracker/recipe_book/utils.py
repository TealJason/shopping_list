import os, json
from django.conf import settings

def addRecipe(ingredients_list, recipe_name):
    path = os.path.join(settings.BASE_DIR, "recipe_book", "data", f"{recipe_name}.json")
    with open(path, "a") as f:
        json.dump({recipe_name: ingredients_list}, f)
        f.write("\n")
