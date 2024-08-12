from rest_framework import serializers
from .models import *


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "gender",
            "profile_picture",
            "profile_url",
            "is_admin_user",
            "is_customer",
        ]


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=20)
