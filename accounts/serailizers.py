from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer

class RegisterSerailizer(ModelSerializer):
    password = serializers.CharField()
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ["username","password","password2"]

    def validate(self,data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        if User.objects.filter(username=data["username"]).exists():
            raise serializers.ValidationError("User with this username already exists")
        return data

    def create(self,validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(**validated_data)
        return user


class Userserailizer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email"]
