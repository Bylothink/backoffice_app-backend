from django.contrib import admin

from .models import Order, Order_Line, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class OrderLineInline(admin.TabularInline):
    model = Order_Line
    extra = 1
    fields = ('product', 'quantity', 'price', 'total')
    readonly_fields = ('price', 'total')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'total')
    inlines = (OrderLineInline, )
    readonly_fields = ('total', )
