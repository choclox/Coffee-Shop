from django.urls import path
from .views import ProductFormView, ProductListView, ProductListAPI

urlpatterns = [
    path('agregar/', ProductFormView.as_view(), name='add_product'),
    path('listar/', ProductListView.as_view(), name='list_products'),
    path('api/', ProductListAPI.as_view(), name='list_products_api'),
]