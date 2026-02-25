from django.db import models
from decimal import Decimal


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    discout = models.BooleanField(default=False)
    image = models.ImageField(upload_to="food_img", blank=True, null=True)
    old_price = models.FloatField(default=100)
    rating = models.PositiveIntegerField(default=1, null=True, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def price(self):
        if self.discout:
            # 30% off
            new_price = self.old_price - ((30 / 100) * self.old_price)
        else:
            new_price = self.old_price

        return new_price
