from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[RegexValidator(
            regex=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
            message="Please provide a valid email address"
        )]
    )
    password = serializers.CharField(write_only=True)
