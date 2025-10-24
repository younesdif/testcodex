"""Tests for the products application."""

from django.test import TestCase
from django.urls import reverse

from .models import Product


class ProductCreateViewTests(TestCase):
    def test_create_product(self):
        response = self.client.post(
            reverse("product-create"),
            {"name": "Test", "description": "Produit de test", "price": "9.99"},
            follow=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Product.objects.filter(name="Test").exists())
        self.assertContains(response, "a été créé avec succès")
