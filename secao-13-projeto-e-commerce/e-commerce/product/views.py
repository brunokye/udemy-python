from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product, Variation
from userprofile.models import UserProfile


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
        # if self.request.session.get("cart"):
        #     del self.request.session["cart"]
        #     self.request.session.save()

        http_referer = self.request.META.get(
            "HTTP_REFERER", reverse("product:list")
        )
        variation_id = self.request.GET.get("vid")

        if not variation_id:
            messages.error(self.request, "O produto não existe.")
            return redirect(http_referer)

        variation = get_object_or_404(Variation, id=variation_id)
        variation_stock = variation.stock
        product = variation.product

        product_id = product.pk
        product_name = product.name
        variation_name = variation.name or ""
        unitary_price = variation.price
        unitary_promotional_price = variation.price_promotional
        quantity = 1
        slug = product.slug
        image = product.image.url

        if variation.stock < 1:
            messages.error(self.request, "Estoque insuficiente.")
            return redirect(http_referer)

        if not self.request.session.get("cart"):
            self.request.session["cart"] = {}
            self.request.session.save()

        cart = self.request.session["cart"]

        if variation_id in cart:
            cart_quantity = cart[variation_id]["quantity"]
            cart_quantity += 1

            if variation_stock < cart_quantity:
                messages.error(
                    self.request,
                    f"Estoque insuficiente para {cart_quantity}x "
                    f"no produto {product_name}. Adicionamos "
                    f"{variation_stock}x no seu carrinho.",
                )

                cart_quantity = variation_stock

            cart[variation_id]["quantity"] = cart_quantity
            cart[variation_id]["quantitative_price"] = (
                unitary_price * cart_quantity
            )
            cart[variation_id]["quantitative_promotional_price"] = (
                unitary_promotional_price * cart_quantity
            )
        else:
            cart[variation_id] = {
                "product_id": product_id,
                "product_name": product_name,
                "variation_name": variation_name,
                "variation_id": variation_id,
                "unitary_price": unitary_price,
                "unitary_promotional_price": unitary_promotional_price,
                "quantitative_price": unitary_price,
                "quantitative_promotional_price": unitary_promotional_price,
                "quantity": quantity,
                "slug": slug,
                "image": image,
            }

        self.request.session.save()

        messages.success(
            self.request,
            f"Produto {product_name} {variation_name} adicionado ao "
            f"carrinho {cart[variation_id]['quantity']}x.",
        )

        return redirect(http_referer)


class ProductRemoveItem(View):
    def get(self, *args, **kwargs):
        http_referer = self.request.META.get(
            "HTTP_REFERER", reverse("product:list")
        )
        variation_id = self.request.GET.get("vid")

        if not variation_id:
            return redirect(http_referer)

        if not self.request.session.get("cart"):
            return redirect(http_referer)

        if variation_id not in self.request.session["cart"]:
            return redirect(http_referer)

        cart = self.request.session["cart"][variation_id]
        messages.success(
            self.request,
            f"Produto { cart['product_name'] } removido do carrinho.",
        )

        del self.request.session["cart"][variation_id]
        self.request.session.save()

        return redirect(http_referer)


class ProductCart(View):
    def get(self, *args, **kwargs):
        context = {
            "cart": self.request.session.get("cart"),
        }
        return render(self.request, "product/cart.html", context)


class ProductCheckout(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("profile:create")

        profile = UserProfile.objects.get(
            user=self.request.user
        ).exists()  # type:ignore

        if not profile:
            messages.error(self.request, "Usuário sem perfil.")
            return redirect("profile:create")

        if not self.request.session.get("cart"):
            messages.error(self.request, "Carrinho vazio.")
            return redirect("product:list")

        context = {
            "user": self.request.user,
            "cart": self.request.session["cart"],
        }

        return render(self.request, "product/checkout.html", context)
