from rest_framework import serializers
from .models import CartItem
from products.serializers import ProductSerializer


class CartItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ["id", "product", "quantity", "size"]