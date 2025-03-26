from django.db import models


class Product(models.Model):
    class Meta:
        db_table = 'store_products'
        verbose_name = "product"
        verbose_name_plural = "products"

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:  # pylint: disable=invalid-str-returned
        return self.name


class Order(models.Model):
    class Meta:
        db_table = 'store_orders'
        verbose_name = "order"
        verbose_name_plural = "orders"

    name = models.CharField(max_length=100)
    description = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)

    lines: models.QuerySet['Order_Line']

    def save(self, *args, **kwargs) -> None:
        self.total = self.lines.aggregate(models.Sum('total'))['total__sum'] or 0.00

        super().save(*args, **kwargs)

    def __str__(self) -> str:  # pylint: disable=invalid-str-returned
        return self.name


class Order_Line(models.Model):  # pylint: disable=invalid-name
    class Meta:
        db_table = 'store_orders_lines'
        verbose_name = "order line"
        verbose_name_plural = "order lines"

    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='lines')
    product = models.ForeignKey(Product, on_delete=models.RESTRICT, related_name='+')

    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    quantity = models.PositiveIntegerField(default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs) -> None:
        self.price = self.product.price
        self.total = self.price * self.quantity

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.order.name} - {self.product.name} (x{self.quantity})"
