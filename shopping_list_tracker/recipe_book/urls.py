from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("recipe_book/", views.recipe_book, name="recipe_book"),
    path("recipe_book/addRecipe/", views.addRecipe, name="addRecipe"),  
    path("recipe_book/removeRecipe/", views.removeRecipe, name="removeRecipe"),
    path("edit/<str:recipe_name>/", views.editRecipe, name="editRecipe"),
    path("update/<str:recipe_name>/", views.updateRecipe, name="updateRecipe"),
    path("editRecipeCard/<str:recipe_name>/", views.editRecipeCard, name="editRecipeCard"),
    path("updateRecipeCard/<str:recipe_name>/", views.updateRecipeCard, name="updateRecipeCard"),
]
