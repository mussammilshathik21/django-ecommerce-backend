from django.urls import path
from .views import (
    product_list,
    product_detail,
    toggle_favorite,
    view_favorites,
    trending_products
)

urlpatterns = [

    # PRODUCTS
    path('', product_list),
    path('trending/',trending_products),


    path('<int:pk>/', product_detail),

    # FAVORITES
    path('favorites/', view_favorites),
    path('favorites/toggle/', toggle_favorite),

]