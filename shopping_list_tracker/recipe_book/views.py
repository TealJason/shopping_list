from django.shortcuts import render

# Create your views here.
def recipe_book(request): 
    return render(request, "recipe_book.html")