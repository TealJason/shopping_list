from django.shortcuts import render
from . import utils
from django.http import request
import json
import os
from django.conf import settings

# Create your views here.
def recipe_book(request): 
    
    path = os.path.join(settings.BASE_DIR, "recipe_book", "data", f"recipe_book.json")

    with open(path) as f:
        recipes = json.load(f)
            
    return render(request, "recipe_book.html",{'recipes': recipes})

def addRecipe(request):
    if request.method == "POST":
        ingredients_list = request.POST["ingredients"].split(",")
        recipe_name = request.POST["recipename"].strip()
        utils.addRecipe(ingredients_list, recipe_name)
        path = os.path.join(settings.BASE_DIR, "recipe_book", "data", f"recipe_book.json")

        with open(path) as f:
            recipes = json.load(f)

        return render(request, "recipe_book.html", {'recipes': recipes})

def removeRecipe(request):
    if request.method == "POST":
        recipe_name = request.POST["recipename"].strip()
        utils.removeRecipe(recipe_name)
        path = os.path.join(settings.BASE_DIR, "recipe_book", "data", f"recipe_book.json")

        with open(path) as f:
            recipes = json.load(f)

        return render(request, "recipe_book.html", {'recipes': recipes})