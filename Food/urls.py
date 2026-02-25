from django.urls import path
from . import views


urlpatterns = [
    path("foods/", views.FoodList.as_view(), name="food_list"),
    path("food/create", views.FoodCreate.as_view(), name="food_create"),
    path("food/<int:pk>", views.Api_Food.as_view(), name="food"),
    path("food_detail/<int:pk>", views.DetailFood.as_view(), name="food_detail"),
]
