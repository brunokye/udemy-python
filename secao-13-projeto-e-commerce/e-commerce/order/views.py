from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from product.models import Variation


class Pay(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, "Você precisa fazer login.")
            return redirect("profile:create")

        if not self.request.session.get("cart"):
            messages.error(self.request, "Carrinho vazio.")
            return redirect("product:list")

        cart = self.request.session.get("cart")
        cart_variation_id = [v for v in cart]
        db_variations = list(
            Variation.objects.select_related("product").filter(
                id__in=cart_variation_id
            )
        )

        for variation in db_variations:
            variation_id = variation.id
            stock = variation.stock
            qtt_cart = cart[variation_id]["quantity"]
            unitary_price = cart[variation_id]["unitary_price"]
            unitary_promotional_price = cart[variation_id][
                "unitary_promotional_price"
            ]

            if stock < qtt_cart:
                cart[variation_id]["quantity"] = stock
                cart["quantitative_price"] = stock * unitary_price
                cart["quantitative_promotional_price"] = (
                    stock * unitary_promotional_price
                )

                messages.error(
                    self.request,
                    "Estoque insuficiente, valores corrigidos, "
                    "verifique seu carrinho.",
                )

                self.request.session.save()
                return redirect("product:list")

        context = {}
        return render(self.request, "order/pay.html", context)


class SaveOrder(View):
    pass


class Detail(View):
    pass
