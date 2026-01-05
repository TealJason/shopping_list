from django.shortcuts import render
from . import utils

def current_meals(request): 
    return render(request, "current_meals.html")

def check_meals(request):
    available_ingredients = []

    if request.method == "POST":
        # Collect all ingredients into a list
        available_ingredients = request.POST.getlist("available_ingredients")
        available_ingredients = [i.strip() for i in available_ingredients if i.strip()]

        possible_meals = utils.find_possible_meals(available_ingredients)

        return render(request, "check_meals.html", {
            "available_ingredients": available_ingredients,
            "possible_meals": possible_meals
        })

    return render(request, "check_meals.html")
