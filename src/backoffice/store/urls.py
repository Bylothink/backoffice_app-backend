from django.urls import path

from .views import OrderListView, OrderLineListView, ProductListView


urlpatterns = [
    path('orders/', OrderListView.as_view()),
    path('orders/<int:order_id>/lines/', OrderLineListView.as_view()),

    path('products/', ProductListView.as_view()),
]
