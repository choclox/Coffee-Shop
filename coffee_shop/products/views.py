from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from products.models import Product
from .forms import ProductForm

# Create your views here.
class ProductFormView(generic.FormView):
    template_name = 'products/add_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('list_products')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ProductListView(generic.ListView):
    template_name = 'products/list_products.html'
    model = Product
    context_object_name = 'products'
