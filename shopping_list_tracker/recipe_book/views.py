from django.shortcuts import render
from . import utils
from django.http import request

# Create your views here.
def recipe_book(request): 
    return render(request, "recipe_book.html")

def addRecipe(request):
    if request.method == "POST":
        ingredients_list = request.POST["ingredients"].split(",")
        recipe_name = request.POST["recipename"].strip()
        utils.addRecipe(ingredients_list, recipe_name)
    return render(request, "recipe_book.html")
