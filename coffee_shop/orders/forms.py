from django.forms import ModelForm    
from .models import OrderItem

class OrderProductForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product']
