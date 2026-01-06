from django.shortcuts import render
from . import utils
from django.conf import settings
import os

def current_meals(request): 
    fridge_path = os.path.join(settings.BASE_DIR, "data", "fridge.csv")
    fridge_items = []
    
    with open(fridge_path) as f:
        for line in f.readlines():
            fridge_items.append(line)
    
    return render(request, "current_meals.html", {"fridge_items":fridge_items})

def update_or_check_fridge(request):
    if request.method == "POST":
        ingredients = request.POST.getlist("ingredients")
        ingredients = [i.strip() for i in ingredients if i.strip()]

        action = request.POST.get("action")
        remove = request.POST.get("remove") == "1"

        if action == "check":
            possible_meals = utils.find_possible_meals()
            return render(request, "current_meals.html", {
                "possible_meals": possible_meals
            })

        utils.write_fridge_csv(ingredients, remove)
        return render(request, "current_meals.html")

    return render(request, "current_meals.html")
