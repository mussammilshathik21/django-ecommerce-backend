from django.urls import path

from .views import register, profile

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [

    path('register/', register),

    path('login/', TokenObtainPairView.as_view()),

    path('token/refresh/', TokenRefreshView.as_view()),

    path('profile/', profile),
]