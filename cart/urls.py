from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart

urlpatterns = [

    path("add/", add_to_cart),
    path("", view_cart),
    path("remove/<int:pk>/", remove_from_cart),

]