"""Tests for the styles application."""

from decimal import Decimal

from django.test import TestCase

from products.models import Product

from .models import Style, SupStyle


class StyleRelationshipsTests(TestCase):
    """Ensure the many-to-many relationships are configured correctly."""

    def setUp(self):
        self.supstyle = SupStyle.objects.create(name="Collection Premium")
        self.style = Style.objects.create(name="Moderne")
        self.style.supstyles.add(self.supstyle)
        self.product = Product.objects.create(
            name="Canapé", description="Confortable", price=Decimal("599.99")
        )
        self.product.styles.add(self.style)

    def test_product_has_styles(self):
        self.assertIn(self.style, self.product.styles.all())

    def test_style_has_supstyles(self):
        self.assertIn(self.supstyle, self.style.supstyles.all())

    def test_supstyle_related_styles(self):
        self.assertIn(self.style, self.supstyle.styles.all())
