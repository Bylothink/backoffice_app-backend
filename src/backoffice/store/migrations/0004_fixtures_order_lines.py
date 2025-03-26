# pylint: disable=invalid-name

from django.apps.registry import Apps

from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor as SchemaEditor

from django.db.models import Model


def create_order_line(order: Model, product: Model, quantity: int) -> None:
    order.lines.create(product=product, quantity=quantity, price=product.price,
                                                           total=product.price * quantity)

def create_order_lines(order: Model, products: list[tuple[Model, int]]) -> None:
    for product, quantity in products:
        create_order_line(order, product, quantity)

    order.save()


def create_fixtures(apps: Apps, schema_editor: SchemaEditor) -> None:
    Product = apps.get_model('store', 'Product')
    Order = apps.get_model('store', 'Order')

    create_order_lines(Order.objects.get(name="Order #1749"), (
        (Product.objects.get(name="Apple"), 1),
        (Product.objects.get(name="Mattress"), 8),
        (Product.objects.get(name="Cauldron"), 1)
    ))
    create_order_lines(Order.objects.get(name="Order #2391"), (
        (Product.objects.get(name="Mattress"), 1),
        (Product.objects.get(name="Spinning Wheel"), 1)
    ))
    create_order_lines(Order.objects.get(name="Order #2764"), (
        (Product.objects.get(name="Pea"), 1),
        (Product.objects.get(name="Ladder"), 1),
        (Product.objects.get(name="Mattress"), 20)
    ))
    create_order_lines(Order.objects.get(name="Order #3401"), (
        (Product.objects.get(name="Magic Bean"), 5),
        (Product.objects.get(name="Ladder"), 1),
        (Product.objects.get(name="Watering Can"), 1)
    ))


class Migration(migrations.Migration):
    dependencies = [('store', '0003_remove_order_products_order_total_order_line')]
    operations = [migrations.RunPython(create_fixtures)]
