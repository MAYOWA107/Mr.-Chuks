from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
)
from .serializers import FoodSerializer
from .models import FoodItem
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .filters import FoodFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from drf_yasg.utils import swagger_auto_schema


class FoodList(ListAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = FoodFilter
    search_fields = ["name", "description"]
    ordering_fields = ["old_price"]
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]


class FoodCreate(CreateAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAdminUser]


class Api_Food(RetrieveUpdateDestroyAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAdminUser]


class DetailFood(RetrieveAPIView):
    queryset = FoodItem.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [AllowAny]
