from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("current_meals/", views.current_meals, name="current_meals"),  # main app logic
    path("update_or_check_fridge/", views.update_or_check_fridge, name="update_or_check_fridge"),
]