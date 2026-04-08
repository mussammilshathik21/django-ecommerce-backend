from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile


# ===============================
# REGISTER SERIALIZER
# ===============================
class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password"
        ]

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )

        # create empty profile automatically
        Profile.objects.create(user=user)

        return user


# ===============================
# USER BASIC INFO
# ===============================
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email"
        ]


# ===============================
# PROFILE SERIALIZER
# ===============================
class ProfileSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    email = serializers.CharField(
        source="user.email",
        read_only=True
    )

    class Meta:
        model = Profile
        fields = [
            "username",
            "email",
            "phone",
            "address",
            "profile_pic"
        ]