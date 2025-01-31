from django.urls import path
from orders.views import MyOrderView,CreateOrderProductView

urlpatterns = [
    path("mi-pedido/", MyOrderView.as_view(), name="my_order"),
    path("crear-producto-orden/", CreateOrderProductView.as_view(), name="add-product"),
]
