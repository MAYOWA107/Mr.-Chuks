from django.urls import path
from . import views


urlpatterns = [
    path("cart/create", views.CartViewCreate.as_view(), name="cart_create"),
    path("cart/<int:pk>", views.CartViewDetail.as_view(), name="cart_detail"),
    path("cartfoods", views.CartFoodView.as_view(), name="cartfoods"),
    path(
        "cartfood/<int:pk>",
        views.CartFoodDetailView().as_view(),
        name="cartfood_detail",
    ),
    path("cartfood/create", views.AddCartFoodView.as_view(), name="cartfood_create"),
    path("orders", views.OrderView.as_view(), name="order"),
    path("order/<int:pk>", views.OrderViewDetail.as_view(), name="order_detail"),
]
