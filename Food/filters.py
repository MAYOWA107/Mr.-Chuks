from django_filters.rest_framework import FilterSet
from .models import FoodItem


class FoodFilter(FilterSet):
    class Meta:
        model = FoodItem
        fields = {
            # "name": ["exact"],
            "old_price": ["gt", "lt"],
        }
