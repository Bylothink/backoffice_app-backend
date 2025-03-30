# pylint: disable=invalid-name

from django.apps.registry import Apps

from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor as SchemaEditor
from django.db.models import Model


def create_order_lines(order: Model, products: list[tuple[Model, int]]) -> None:
    for product, quantity in products:
        total = product.price * quantity
        order.lines.create(product=product, quantity=quantity, price=product.price, total=total)

    order.save()


def create_fixtures(apps: Apps, schema_editor: SchemaEditor) -> None:
    Product = apps.get_model('store', 'Product')
    Product.objects.bulk_create([
        Product(name="Apple", price=0.49),
        Product(name="Ladder", price=49.98),
        Product(name="Magic Bean", price=5.99),
        Product(name="Mattress", price=299.49),
        Product(name="Pea", price=0.98),
        Product(name="Cauldron", price=95.95),
        Product(name="Spinning Wheel", price=149.99),
        Product(name="Watering Can", price=14.95)
    ])

    Order = apps.get_model('store', 'Order')
    Order.objects.bulk_create([
        Order(name="Order #1749", description="Raven's Hollow Castle - Darkwood Forest, Enchanted Kingdom"),
        Order(name="Order #2391", description="Forbidden Spire - Shadowvale, Cursed Lands"),
        Order(name="Order #2764", description="Royal Featherbed Palace - Silkvale, Kingdom of Slumber"),
        Order(name="Order #3401", description="Humble Cottage - Meadow's End, Smallfolk Village")
    ])

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
    dependencies = [('store', '0001_initial')]
    operations = [migrations.RunPython(create_fixtures)]
