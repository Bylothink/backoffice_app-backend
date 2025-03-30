from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Order
from ..serializers import OrderLineDetailsSerializer, OrderLineListSerializer


class OrderLineListView(APIView):
    def get(self, request: Request, order_id: int) -> Response:
        offset = int(request.query_params.get('offset', '0'))
        limit = int(request.query_params.get('limit', '10'))

        order = get_object_or_404(Order, pk=order_id)
        lines = order.lines.all()[offset:offset + limit]
        serializer = OrderLineListSerializer(lines, many=True)

        return Response(serializer.data)

    def post(self, request: Request, order_id: int) -> Response:
        order = get_object_or_404(Order, pk=order_id)

        request.data['order'] = order_id
        serializer = OrderLineDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(order=order)

            serializer = OrderLineListSerializer(order.lines.last())
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderLineDetailView(APIView):
    def get(self, request: Request, order_id: int, line_id: int) -> Response:
        order = get_object_or_404(Order, pk=order_id)
        line = get_object_or_404(order.lines, pk=line_id)
        serializer = OrderLineListSerializer(line)

        return Response(serializer.data)

    def put(self, request: Request, order_id: int, line_id: int) -> Response:
        order = get_object_or_404(Order, pk=order_id)
        line = get_object_or_404(order.lines, pk=line_id)

        request.data['order'] = order_id
        serializer = OrderLineDetailsSerializer(line, data=request.data)
        if serializer.is_valid():
            serializer.save()

            serializer = OrderLineListSerializer(line)
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, order_id: int, line_id: int) -> Response:
        order = get_object_or_404(Order, pk=order_id)
        line = get_object_or_404(order.lines, pk=line_id)
        line.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
