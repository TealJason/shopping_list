from django.shortcuts import render
from . import utils
from django.http import request
import json
import os
from django.conf import settings
from django.shortcuts import render, redirect
from urllib.parse import unquote

# Create your views here.
def recipe_book(request): 
    
    path = os.path.join(settings.BASE_DIR,  "data", f"recipe_book.json")

    with open(path) as f:
        recipes = json.load(f)
            
    return render(request, "recipe_book.html",{'recipes': recipes})

def addRecipe(request):
    if request.method == "POST":      
        ingredients_list = [i.strip().lower()for i in request.POST["ingredients"].split(",")if i.strip()]
        recipe_name = request.POST["recipename"].strip()
        utils.addRecipe(ingredients_list, recipe_name)
        path = os.path.join(settings.BASE_DIR, "data", f"recipe_book.json")

        with open(path) as f:
            recipes = json.load(f)

        return render(request, "recipe_book.html", {'recipes': recipes})

def removeRecipe(request):
    if request.method == "POST":
        recipe_name = request.POST["recipename"].strip()
        utils.removeRecipe(recipe_name)
        path = os.path.join(settings.BASE_DIR, "data", f"recipe_book.json")

        with open(path) as f:
            recipes = json.load(f)

        return render(request, "recipe_book.html", {'recipes': recipes})

def editRecipe(request, recipe_name):
    recipe_name = unquote(recipe_name)
    recipe = utils.getRecipe(recipe_name)

    if not recipe:
        return redirect("recipe_book")

    return render(request, "edit_recipe.html", {
        "name": recipe_name,
        "ingredients": ", ".join(recipe)
    })

def updateRecipe(request, recipe_name):
    if request.method == "POST":
        recipe_name = unquote(recipe_name)

        new_name = request.POST["recipename"].strip()
        ingredients = [i.strip().lower() for i in request.POST["ingredients"].split(",") if i.strip()]

        utils.updateRecipe(recipe_name, new_name, ingredients)

    return redirect("recipe_book")

def editRecipeCard(request, recipe_name):
    recipe_name = unquote(recipe_name)
    card = utils.getRecipeCard(recipe_name)

    if card is None:
        return redirect("recipe_book")

    return render(request, "view_recipe_card.html", {
        "name": recipe_name,
        "card": card
    })

def updateRecipeCard(request, recipe_name):
    if request.method == "POST":
        recipe_name = unquote(recipe_name)

        new_name = request.POST["recipename"].strip()
        card_text = request.POST.get("recipe_card", "").strip()

        utils.updateRecipeCard(recipe_name, new_name, card_text)

    return redirect("recipe_book")