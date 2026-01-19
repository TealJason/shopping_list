from django.shortcuts import render
import os
import json
from . import utils
from django.conf import settings 

# Create your views here.
def shopping_list(request):
    path = os.path.join(settings.BASE_DIR, "data", "recipe_book.json")
    omit = request.POST.get("omit") is not None
    
    with open(path) as f:
        recipes = json.load(f)

    ingredient_dict = None

    if request.method == "POST":
        selected_meals = request.POST.getlist("meals")
        ingredient_dict = utils.create_shopping_list(selected_meals,omit)

    return render(request, "shopping_list.html", {
        "recipes": recipes,
        "ingredient_dict": ingredient_dict
    })
