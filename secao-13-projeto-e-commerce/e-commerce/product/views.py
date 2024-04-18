# from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = "product/list.html"
    context_object_name = "products"
    paginate_by = 1


class ProductDetail(DetailView):
    model = Product
    template_name = "product/detail.html"
    context_object_name = "product"
    slug_url_kwarg = "slug"


class ProductAddItem(View):
    pass


class ProductRemoveItem(View):
    pass


class ProductCart(View):
    pass


class ProductCheckout(View):
    pass
