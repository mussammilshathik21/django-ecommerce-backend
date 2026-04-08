from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User

from .models import Profile
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    ProfileSerializer
)


# ===============================
# REGISTER USER
# ===============================
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):

    serializer = RegisterSerializer(data=request.data)

    if serializer.is_valid():

        serializer.save()

        return Response({
            "message": "User registered successfully"
        })

    return Response(serializer.errors)


# ===============================
# GET / UPDATE PROFILE
# ===============================
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    # GET PROFILE
    if request.method == "GET":

        serializer = ProfileSerializer(profile)

        return Response(serializer.data)

    # UPDATE PROFILE
    if request.method == "PUT":

        serializer = ProfileSerializer(
            profile,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)