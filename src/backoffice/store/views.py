from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, Product
from .serializers import OrderListSerializer, OrderLineSerializer, ProductListSerializer


class OrderListView(APIView):
    def get(self, request: Request) -> Response:
        offset = int(request.query_params.get('offset', '0'))
        limit = int(request.query_params.get('limit', '10'))

        orders = Order.objects.all()[offset:offset + limit]
        serializer = OrderListSerializer(orders, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = OrderListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderLineListView(APIView):
    def get(self, request: Request, order_id: int) -> Response:
        offset = int(request.query_params.get('offset', '0'))
        limit = int(request.query_params.get('limit', '10'))

        order = get_object_or_404(Order, pk=order_id)
        lines = order.lines.all()[offset:offset + limit]
        serializer = OrderLineSerializer(lines, many=True)

        return Response(serializer.data)


class ProductListView(APIView):
    def get(self, request: Request) -> Response:
        offset = int(request.query_params.get('offset', '0'))
        limit = int(request.query_params.get('limit', '10'))

        products = Product.objects.all()[offset:offset + limit]
        serializer = ProductListSerializer(products, many=True)

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = ProductListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
