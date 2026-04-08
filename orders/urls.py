from django.urls import path
from .views import create_order, view_orders

urlpatterns = [

    path("create/", create_order),

    path("", view_orders),

]