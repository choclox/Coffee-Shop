from django.views.generic import DetailView
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class MyOrderView(LoginRequiredMixin,DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order"
    
    def get_object(self, queryset=None):
        return Order.objects.filter(user= self.request.user,is_active=True).first()
       