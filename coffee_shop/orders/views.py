from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Order, OrderItem
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import OrderProductForm


# Create your views here.
class MyOrderView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"

    def get_object(self, queryset=None):
        return Order.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_orders"] = Order.objects.filter(
            user=self.request.user, is_active=True
        )
        context["inactive_orders"] = Order.objects.filter(
            user=self.request.user, is_active=False
        )
        return context


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    form_class = OrderProductForm
    template_name = "orders/create_order_product.html"
    success_url = reverse_lazy("my_order")

    def form_valid(self, form):
        order, _ = Order.objects.get_or_create(is_active=True, user=self.request.user)

        # Obtener el producto del formulario
        product = form.cleaned_data["product"]

        # Buscar si ya existe el producto en la orden
        order_item = OrderItem.objects.filter(order=order, product=product).first()
        if order_item:
            form.instance.quantity = (
                order_item.quantity + 1
            )  # Si existe, aumentar cantidad
            order_item.delete()
        else:
            form.instance.quantity = 1  # Si no existe, crearlo y establecer cantidad

        form.instance.order = order  # Establecer la orden en el formulario
        form.instance.save()
        return super().form_valid(form)
