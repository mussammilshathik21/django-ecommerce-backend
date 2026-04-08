from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Banner


@api_view(['GET'])
@permission_classes([AllowAny])
def get_banner(request):

    banner = Banner.objects.filter(is_active=True).first()

    if not banner:
        return Response({"message": "No banner found"})

    return Response({
        "title": banner.title,
        "subtitle": banner.subtitle,
        "image": banner.image.url
    })