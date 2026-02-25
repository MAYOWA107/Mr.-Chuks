from django.shortcuts import render
from .models import Cart, CartFood, Order, OrderFood
from .serializers import (
    CartSerializer,
    CartFoodSerializer,
    AddCartFoodSerializer,
    OrderSerializer,
    OrderFoodSerializer,
    CreateOrderSerializer,
)
from rest_framework.generics import (
    CreateAPIView,
    RetrieveDestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
)

from rest_framework.permissions import IsAuthenticated, AllowAny


class CartViewCreate(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]


class CartViewDetail(RetrieveDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [AllowAny]


class CartFoodView(ListAPIView):
    queryset = CartFood.objects.all()
    serializer_class = CartFoodSerializer


class CartFoodDetailView(RetrieveUpdateDestroyAPIView):
    queryset = CartFood.objects.all()
    serializer_class = CartFoodSerializer
    permission_classes = [AllowAny]


class AddCartFoodView(CreateAPIView):
    queryset = CartFood.objects.all()
    serializer_class = AddCartFoodSerializer
    permission_classes = [AllowAny]


class OrderView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateOrderSerializer

        return OrderSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user_id"] = self.request.user.id
        return context


class OrderViewDetail(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=user)


class OrderFoodView(ListCreateAPIView):
    queryset = OrderFood.objects.all()
    serializer_class = OrderFoodSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return OrderFood.objects.all()
        return OrderFood.objects.filter(order__user=user)
