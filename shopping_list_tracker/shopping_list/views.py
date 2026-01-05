from django.shortcuts import render
import os
import json
from . import utils
from django.conf import settings 

# Create your views here.
def shopping_list(request): 
    path = os.path.join(settings.BASE_DIR, "data", f"recipe_book.json")
    with open (path) as f:
        recipes = json.load(f)
    
    return render(request, "shopping_list.html",{'recipes': recipes})

def create_shopping_list(request):
    path = os.path.join(settings.BASE_DIR, "data", f"recipe_book.json")

    with open (path) as f:
        recipes = json.load(f)
        
    utils.create_shopping_list()
    
    return render(request, "shopping_list.html",{'recipes': recipes})