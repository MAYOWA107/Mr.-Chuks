from django.db import models
from django.conf import settings
from Food.models import FoodItem


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)


class CartFood(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, blank=True, null=True, related_name="fooditems"
    )
    food_item = models.ForeignKey(
        FoodItem,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="fooditems",
    )
    quantity = models.IntegerField(default=0)


class Order(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("CONFIRMED", "Confirmed"),
        ("PREPARING", "Preparing"),
        ("OUT_OF_DELIVERY", "Out_for_Delivery"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status


class OrderFood(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name="fooditems")
    food_item = models.ForeignKey(FoodItem, on_delete=models.PROTECT)
    quantity = models.PositiveBigIntegerField()

    def __str__(self):
        return self.food_item.name
