from rest_framework.serializers import ModelSerializer

from .models import Order, Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class OrderListSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'name', 'description')


class OrderDetailsSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
