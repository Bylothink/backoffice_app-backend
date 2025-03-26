from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Product
from ..serializers import ProductDetailsSerializer, ProductListSerializer


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


class ProductDetailView(APIView):
    def get(self, request: Request, product_id: int) -> Response:
        product = get_object_or_404(Product, pk=product_id)
        serializer = ProductDetailsSerializer(product)

        return Response(serializer.data)

    def put(self, request: Request, product_id: int) -> Response:
        product = get_object_or_404(Product, pk=product_id)
        serializer = ProductDetailsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, product_id: int) -> Response:
        product = get_object_or_404(Product, pk=product_id)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
