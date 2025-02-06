from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "users/sign_up.html"
    success_url = reverse_lazy("login")
