from rest_framework import serializers
from .models import Cart, CartFood, Order, OrderFood
from Food.serializers import FoodSerializer
from Food.models import FoodItem
from django.db import transaction


class SimpleFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ["id", "name", "price"]


class CartFoodSerializer(serializers.ModelSerializer):
    food_item = SimpleFoodSerializer()
    sub_total = serializers.SerializerMethodField(method_name="total")

    class Meta:
        model = CartFood
        fields = ["id", "cart", "food_item", "quantity", "sub_total"]

    def total(self, cartfood: CartFood):
        return cartfood.quantity * cartfood.food_item.price


class CartSerializer(serializers.ModelSerializer):
    grand_total = serializers.SerializerMethodField(method_name="main_total")

    class Meta:
        model = Cart
        fields = ["id", "grand_total"]

    def main_total(self, cart: Cart):
        all_foods = cart.fooditems.all()
        total = sum([food.quantity * food.food_item.price for food in all_foods])
        return total


class AddCartFoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartFood
        fields = [
            "id",
            "cart",
            "food_item",
            "quantity",
        ]


class OrderFoodSerializer(serializers.ModelSerializer):
    food_item = SimpleFoodSerializer()

    class Meta:
        model = OrderFood
        fields = ["id", "order", "food_item", "quantity"]


class OrderSerializer(serializers.ModelSerializer):
    foods = OrderFoodSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ["id", "status", "foods", "created_at", "user"]


class CreateOrderSerializer(serializers.Serializer):
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all())

    class Meta:
        model = Order
        fields = ["cart"]

    def save(self, **kwargs):
        user = self.context["request"].user
        cart = self.validated_data["cart"]
        # helps reverse operation when any operation fails
        # Ensuring all operations are carried out with transaction atomic
        with transaction.atomic():

            order = Order.objects.create(user=user)
            cartfood = CartFood.objects.filter(cart=cart)
            orderfoods = [
                OrderFood(order=order, food_item=food.food_item, quantity=food.quantity)
                for food in cartfood
            ]
            # creating an order of the cart_id
            OrderFood.objects.bulk_create(orderfoods)
            # delete cart when order has been created
            cart.delete()
            return order
