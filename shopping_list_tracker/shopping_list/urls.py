from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("shopping_list/", views.shopping_list, name="shopping_list"),  # main app logic
    path("shopping_list/create_shopping_list/", views.create_shopping_list, name="create_shopping_list"),  
]
