from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart.models import CartItem


# ========================
# CREATE ORDER
# ========================
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_order(request):

    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        return Response({"error": "Cart is empty"}, status=400)

    order = Order.objects.create(
        user=request.user,
        total_price=0
    )

    total = 0

    for item in cart_items:

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price,
            size=item.size
        )

        total += item.product.price * item.quantity

    order.total_price = total
    order.save()

    cart_items.delete()

    return Response({
        "message": "Order placed successfully",
        "order_id": order.id,
        "total_price": order.total_price
    })


# ========================
# GET USER ORDERS
# ========================
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def view_orders(request):

    orders = Order.objects.filter(user=request.user).order_by("-created_at")

    serializer = OrderSerializer(orders, many=True)

    return Response(serializer.data)