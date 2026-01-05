from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("recipe_book/", views.recipe_book, name="recipe_book"),  # main app logic
    path("recipe_book/addRecipe/", views.addRecipe, name="addRecipe"),  
    path("recipe_book/removeRecipe/", views.removeRecipe, name="removeRecipe")
]
