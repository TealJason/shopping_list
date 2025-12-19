from django.shortcuts import render

def current_meals(request): 
    return render(request, "current_meals.html")