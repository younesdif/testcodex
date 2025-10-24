"""Views for the products application."""

from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ProductForm
from .models import Product


class ProductCreateView(CreateView):
    """Display and process the form used to create products."""

    template_name = "products/product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy("product-create")
    model = Product

    def form_valid(self, form):
        """Display a success message after saving the product."""

        response = super().form_valid(form)
        self.request.session["product_created"] = form.instance.name
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_created"] = self.request.session.pop("product_created", None)
        return context
