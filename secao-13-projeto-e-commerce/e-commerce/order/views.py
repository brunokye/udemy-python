from .models import Order, OrderItem
from product.models import Variation
from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from utils import format


class Pay(View):
    def get(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            messages.error(self.request, "Você precisa fazer login.")
            return redirect("profile:create")

        cart = self.request.session.get("cart")

        if not cart:
            messages.error(self.request, "Carrinho vazio.")
            return redirect("product:list")

        cart_product_id = [v for v in cart]

        db_variations = list(
            Variation.objects.select_related("product").filter(
                id__in=cart_product_id
            )
        )

        for variation in db_variations:
            variation_id = str(variation.pk)
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

        qtt_total_cart = format.cart_total_qtt(cart)
        total_cart_value = format.cart_total(cart)

        order = Order(
            user=self.request.user,
            qtt_total=qtt_total_cart,
            total_value=total_cart_value,
            status="C",
        )

        order.save()

        OrderItem.objects.bulk_create(
            [
                OrderItem(
                    order=order,
                    product=variation["product_name"],
                    product_id=variation["product_id"],
                    variation=variation["variation_name"],
                    variation_id=variation["variation_id"],
                    price=variation["quantity_price"],
                    price_promotional=variation["quantity_promotional_price"],
                    quantity=variation["quantity"],
                    image=variation["image"],
                )
                for variation in cart.values()
            ]
        )

        del self.request.session["cart"]

        return redirect("order:list")


class SaveOrder(View):
    pass


class Detail(View):
    pass


class List(View):
    pass
