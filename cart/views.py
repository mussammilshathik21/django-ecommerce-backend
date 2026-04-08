from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import CartItem
from .serializers import CartItemSerializer
from products.models import Product


# ADD TO CART
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_cart(request):

    product_id = request.data.get("product_id")
    quantity = request.data.get("quantity", 1)
    size = request.data.get("size")

    # handle if frontend accidentally sends product object
    if isinstance(product_id, dict):
        product_id = product_id.get("id")

    product = Product.objects.get(id=int(product_id))

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        size=size
    )

    if not created:
        cart_item.quantity += int(quantity)
    else:
        cart_item.quantity = int(quantity)

    cart_item.save()

    serializer = CartItemSerializer(cart_item)

    return Response(serializer.data)


# VIEW CART
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_cart(request):

    items = CartItem.objects.filter(user=request.user)

    serializer = CartItemSerializer(items, many=True)

    return Response(serializer.data)


# REMOVE FROM CART
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, pk):

    try:
        item = CartItem.objects.get(id=pk, user=request.user)
    except CartItem.DoesNotExist:
        return Response({"error": "Item not found"}, status=404)

    item.delete()

    return Response({"message": "Item removed"})