import os, json
from django.conf import settings

def addRecipe(ingredients_list, recipe_name):
    
    path = os.path.join(settings.BASE_DIR, "data", f"recipe_book.json")
    print (path)

    # Read existing data
    with open(path, "r") as f:
        recipe_dictionary = json.loads(f.read())

    try:
        recipe_dictionary[recipe_name] = ingredients_list
    except Exception as e:
        print(f"Error adding recipe: {e}")
        
    # Write updated data back
    with open(path, "w") as f:
        f.write(json.dumps(recipe_dictionary, indent=4))
        
def removeRecipe(recipe_name):
    path = os.path.join(settings.BASE_DIR, "data", f"recipe_book.json")
    
    # Read existing data
    with open(path, "r") as f:
        recipe_dictionary = json.loads(f.read())

    try:
        del recipe_dictionary[recipe_name]
    except KeyError:
        print(f"Recipe '{recipe_name}' not found.")
    except Exception as e:
        print(f"Error removing recipe: {e}")
        
    # Write updated data back
    with open(path, "w") as f:
        f.write(json.dumps(recipe_dictionary, indent=4))
        
def loadRecipes():
    path = os.path.join(settings.BASE_DIR, "data", "recipe_book.json")
    with open(path, "r") as f:
        return json.load(f)

def saveRecipes(recipe_dictionary):
    path = os.path.join(settings.BASE_DIR, "data", "recipe_book.json")
    with open(path, "w") as f:
        f.write(json.dumps(recipe_dictionary, indent=4))

def getRecipe(recipe_name):
    recipes = loadRecipes()
    return recipes.get(recipe_name)

def updateRecipe(old_name, new_name, ingredients_list):
    recipes = loadRecipes()

    # Remove old entry
    if old_name in recipes:
        del recipes[old_name]

    # Write updated
    recipes[new_name] = ingredients_list

    saveRecipes(recipes)

def loadRecipesCards():
    path = os.path.join(settings.BASE_DIR, "data", "recipe_card.json")
    with open(path, "r") as f:
        return json.load(f)


def saveRecipesCard(recipe_dictionary):
    path = os.path.join(settings.BASE_DIR, "data", "recipe_card.json")
    with open(path, "w") as f:
        f.write(json.dumps(recipe_dictionary, indent=4))


def getRecipeCard(recipe_name):
    recipes = loadRecipesCards()
    return recipes.get(recipe_name)


def updateRecipeCard(old_name, new_name, card_text):
    recipes = loadRecipesCards()

    # Remove old entry
    if old_name in recipes:
        del recipes[old_name]

    # Write updated
    recipes[new_name] = card_text

    saveRecipesCard(recipes)