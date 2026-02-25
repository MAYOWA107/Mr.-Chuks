from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from .views import CartViewCreate, CartFoodView, AddCartFoodView, OrderFoodView


class CartTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = CartViewCreate.as_view()
        self.url = reverse("cart_create")

    def authenticate(self):
        self.client.post(
            "auth/users/",
            {
                "email": "testorder@gmail.com",
                "username": "testorder",
                "password": "iamacoder@123",
                "phone_number": "08166717873",
            },
        )

        response = self.client.post(
            reverse("jwt-create"),
            {"email": "testorder@gmail.com", "password": "iamacoder@123"},
        )
        # token = response.data["access"]
        # self.client.credentials(HTTP_AUTHORIZATION=f"JWT {token}")

    def test_cart_create(self):
        self.cart_post = {"id": 1}
        request = self.factory.post(self.url, self.cart_post)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["grand_total"], 0)

    def test_list_food(self):
        self.url = reverse("cartfoods")
        self.view = CartFoodView.as_view()
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_add_food_to_cart(self):
        cart_post = {"cart_id": 1, "food_item_id": 1, "quantity": 5}
        self.url = reverse("cartfood_create")
        self.view = AddCartFoodView.as_view()
        request = self.factory.post(self.url, cart_post)
        response = self.view(request)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_order_food_without_authentication(self):
        self.url = reverse("order")
        self.view = OrderFoodView.as_view()
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
