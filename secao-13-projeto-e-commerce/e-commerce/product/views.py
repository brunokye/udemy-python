# from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from .models import Product


class ProductList(ListView):
    model = Product
    template_name = "product/list.html"
    context_object_name = "products"
    paginate_by = 1


class ProductDetail(View):
    pass


class ProductAddItem(View):
    pass


class ProductRemoveItem(View):
    pass


class ProductCart(View):
    pass


class ProductCheckout(View):
    pass
