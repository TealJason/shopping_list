import os, json
from django.conf import settings

def addRecipe(ingredients_list, recipe_name):
    
    path = os.path.join(settings.BASE_DIR, "data", f"recipe_book.json")
    

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