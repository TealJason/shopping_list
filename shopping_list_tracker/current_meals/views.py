from django.shortcuts import render
from . import utils
from django.conf import settings
import os

def current_meals(request): 
    fridge_path = os.path.join(settings.BASE_DIR, "data", "fridge.txt")
    fridge_items = []
    
    with open(fridge_path) as f:
        for line in f.readlines():
            fridge_items.append(line)
    
    return render(request, "current_meals.html", {"fridge_items":fridge_items})

def update_or_check_fridge(request):
    fridge_path = os.path.join(settings.BASE_DIR, "data", "fridge.txt")

    if request.method == "POST":
        ingredients = request.POST.getlist("ingredients")
        ingredients = [i.strip().lower() for i in ingredients if i.strip()]

        remove = request.POST.get("remove") == "1"

        utils.write_fridge_csv(ingredients, remove)

    fridge_items = []
    if os.path.exists(fridge_path):
        with open(fridge_path) as f:
            fridge_items = [line.strip() for line in f]

    return render(request, "current_meals.html", {
        "fridge_items": fridge_items
    })