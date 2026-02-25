from rest_framework.serializers import ModelSerializer
from .models import Custom_User
from djoser.serializers import UserCreateSerializer


class SignupSerializer(ModelSerializer):
    class Meta:
        model = Custom_User
        fields = ["email", "phone_number", "username", "password"]

        def create(seldf, validated_data):
            user = Custom_User.objects.create_user(
                username=validated_data.get("email")
                or validated_data.get("phone_number"),
                email=validated_data.get("email"),
                phone_number=validated_data.get("phone_number"),
                password=validated_data.get("password"),
                is_active=False,
            )


class MyUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = [
            "id",
            "email",
            "username",
            "password",
            "phone_number",
            "first_name",
            "last_name",
        ]
