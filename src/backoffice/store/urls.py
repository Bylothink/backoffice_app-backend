from django.urls import path

from . import views


urlpatterns = [
    path('orders/', views.OrderListView.as_view()),
    path('orders/<int:order_id>/', views.OrderDetailView.as_view()),

    path('orders/<int:order_id>/lines/', views.OrderLineListView.as_view()),
    path('orders/<int:order_id>/lines/<int:line_id>/', views.OrderLineDetailView.as_view()),

    path('products/', views.ProductListView.as_view()),
    path('products/<int:product_id>/', views.ProductDetailView.as_view())
]
