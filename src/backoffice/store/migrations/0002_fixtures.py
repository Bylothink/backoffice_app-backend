# pylint: disable=invalid-name

from django.apps.registry import Apps

from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor as SchemaEditor


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

    Order.objects.get(name="Order #1749").products.set((
        Product.objects.get(name="Apple"),
        Product.objects.get(name="Mattress"),
        Product.objects.get(name="Cauldron")
    ))
    Order.objects.get(name="Order #2391").products.set((
        Product.objects.get(name="Mattress"),
        Product.objects.get(name="Spinning Wheel")
    ))
    Order.objects.get(name="Order #2764").products.set((
        Product.objects.get(name="Pea"),
        Product.objects.get(name="Ladder"),
        Product.objects.get(name="Mattress")
    ))
    Order.objects.get(name="Order #3401").products.set((
        Product.objects.get(name="Magic Bean"),
        Product.objects.get(name="Ladder"),
        Product.objects.get(name="Watering Can")
    ))


class Migration(migrations.Migration):
    dependencies = [('store', '0001_initial')]
    operations = [migrations.RunPython(create_fixtures)]
