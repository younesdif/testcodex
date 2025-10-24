"""Forms for the products application."""

from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    """Form allowing users to create new products."""

    class Meta:
        model = Product
        fields = ["name", "description", "price"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nom du produit"}),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "placeholder": "Description du produit"}
            ),
            "price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Prix"}),
        }
