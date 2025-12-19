from django.shortcuts import render

# Create your views here.
def shopping_list(request): 
    return render(request, "shopping_list.html")