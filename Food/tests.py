from rest_framework.test import APITestCase, APIRequestFactory
from django.urls import reverse
from rest_framework import status
from .models import FoodItem
from .views import FoodList, FoodCreate, Api_Food
from accounts.models import Custom_User


# test is for IsAuthenticated


class FoodListTest(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = FoodList.as_view()
        self.url = reverse("food_list")

    def test_food_list(self):
        # test all foodlist
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_food_model(self):
        fooditem = FoodItem.objects.create(name="Dodo")
        self.assertEqual(fooditem.name, "Dodo")


class FoodCreateTest(APITestCase):

    sample_food = {
        "name": "Rice",
        "description": "My Favourite food",
        "discount": False,
        "old_price": 400,
        "available": True,
    }

    def setUp(self):

        self.factory = APIRequestFactory()
        self.view = FoodCreate.as_view()
        self.url = reverse("food_create")
        self.user = Custom_User.objects.create(
            email="test@gmail.com",
            username="test",
            password="iamacoder1@",
            phone_number="09066728964",
            is_staff=True,
        )

    def authenticate(self):
        self.client.post(
            "/auth/users/",
            {
                "email": "testuser@gmail.com",
                "username": "testuser",
                "password": "iamacoder@123",
                "phone_number": "09066713865",
            },
        )
        response = self.client.post(
            reverse("jwt-create"),
            {"email": "testuser@gmail.com", "password": "iamacoder@123"},
        )
        token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"JWT {token}")

    def test_food_create_without_authentication(self):
        request = self.factory.post(self.url, self.sample_food)
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_food_create_with_authentication(self):
        self.authenticate()
        response = self.client.post(self.url, self.sample_food)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], self.sample_food["name"])
