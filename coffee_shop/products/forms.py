from django import forms
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=200)
    description = forms.CharField(label="Descripcion", max_length=500)
    price = forms.DecimalField(label="Precio", max_digits=10, decimal_places=2)
    available = forms.BooleanField(initial=True, label="Disponible", required=False)
    photo = forms.ImageField(label="Foto", required=False)

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            photo=self.cleaned_data["photo"],
        )
