from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


# Create your tests here.
class OrderViewTest(TestCase):

    def test_no_logged_user_should_redirect(self):
        url = reverse("my_order")
        response = self.client.get(url)
        self.assertEqual(response.url, "/usuarios/login/?next=/ordenes/mi-pedido/")
        self.assertEqual(response.status_code, 302)

    def test_logged_user_should_return_200(self):
        url = reverse("my_order")
        user = get_user_model().objects.create_user(username="test")
        self.client.force_login(user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
