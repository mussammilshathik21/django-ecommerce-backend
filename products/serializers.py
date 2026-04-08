from rest_framework import serializers
from .models import Product,Favorite


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):

    product = ProductSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = ["id","product"]