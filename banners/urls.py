from django.urls import path
from .views import get_banner

urlpatterns = [

    path("", get_banner),

]