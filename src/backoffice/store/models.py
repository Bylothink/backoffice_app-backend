from django.db import models


class Product(models.Model):
    class Meta:
        db_table = 'store_products'
        verbose_name = "product"
        verbose_name_plural = "products"

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str: # pylint: disable=invalid-str-returned
        return self.name


class Order(models.Model):
    class Meta:
        db_table = 'store_orders'
        verbose_name = "order"
        verbose_name_plural = "orders"

    name = models.CharField(max_length=100)
    description = models.TextField()
    products = models.ManyToManyField(Product, related_name='orders', db_table='store_orders_products')

    def __str__(self) -> str: # pylint: disable=invalid-str-returned
        return self.name
