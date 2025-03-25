from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, Product
from .serializers import OrderListSerializer, ProductSerializer


class OrderListView(APIView):
    def get(self, request: Request) -> Response:
        offset = request.query_params.get('offset', 0)
        limit = request.query_params.get('limit', 10)

        orders = Order.objects.all()[offset:offset + limit]
        serializer = OrderListSerializer(orders, many=True)

        return Response(serializer.data)
