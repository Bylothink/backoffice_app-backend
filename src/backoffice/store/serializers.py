from rest_framework.serializers import ModelSerializer, ReadOnlyField

from .models import Order, Order_Line, Product


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name', 'description', 'total')


class OrderDetailsSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderLineListSerializer(ModelSerializer):
    product_name = ReadOnlyField(source='product.name')

    class Meta:
        model = Order_Line
        fields = ('id', 'order_id', 'product_id', 'product_name', 'price', 'quantity', 'total')


class OrderLineDetailsSerializer(ModelSerializer):
    class Meta:
        model = Order_Line
        fields = '__all__'


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class ProductDetailsSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
