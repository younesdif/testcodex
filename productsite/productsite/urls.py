"""productsite URL Configuration."""

from django.contrib import admin
from django.urls import path

from products.views import ProductCreateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ProductCreateView.as_view(), name="product-create"),
]
