from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product, Favorite
from .serializers import ProductSerializer, FavoriteSerializer


# ===============================
# PRODUCT LIST
# ===============================
@api_view(['GET'])
@permission_classes([AllowAny])
def product_list(request):

    category = request.GET.get('category')

    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)



# ===============================
# TRENDING PRODUCTS
# ===============================
@api_view(['GET'])
@permission_classes([AllowAny])
def trending_products(request):

    products = Product.objects.filter(is_trending=True)

    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


# ===============================
# PRODUCT DETAIL
# ===============================
@api_view(['GET'])
@permission_classes([AllowAny])
def product_detail(request, pk):

    product = get_object_or_404(Product, id=pk)

    serializer = ProductSerializer(product)

    return Response(serializer.data)


# ===============================
# TOGGLE FAVORITE (ADD / REMOVE)
# ===============================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggle_favorite(request):

    product_id = request.data.get("product_id")

    favorite = Favorite.objects.filter(
        user=request.user,
        product_id=product_id
    ).first()

    # If already exists → remove
    if favorite:
        favorite.delete()
        return Response({
            "status": "removed"
        })

    # If not exists → add
    Favorite.objects.create(
        user=request.user,
        product_id=product_id
    )

    return Response({
        "status": "added"
    })


# ===============================
# VIEW FAVORITES
# ===============================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_favorites(request):

    favorites = Favorite.objects.filter(user=request.user)

    serializer = FavoriteSerializer(favorites, many=True)

    return Response(serializer.data)