from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, Variation


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
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            "HTTP_REFERER", reverse("product:list")
        )
        variation_id = self.request.GET.get("vid")

        if not variation_id:
            messages.error(self.request, "O produto não existe.")
            return redirect(http_referer)

        variation = get_object_or_404(Variation, id=variation_id)

        if not self.request.session.get("cart"):
            self.request.session["cart"] = {}
            self.request.session.save()

        cart = self.request.session["cart"]

        if variation_id in cart:
            pass
        else:
            pass

        return HttpResponse(f"{variation.product} {variation.name}")


class ProductRemoveItem(View):
    pass


class ProductCart(View):
    pass


class ProductCheckout(View):
    pass
