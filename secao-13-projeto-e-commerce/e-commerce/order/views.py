from .models import Order, OrderItem
from product.models import Variation
from django.views import View
from django.views.generic import DetailView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from utils import format


class DispatchLoginRequired(View):
    def dispatch(self, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("profile:create")

        return super().dispatch(*args, **kwargs)


class Pay(DispatchLoginRequired, DetailView):
    template_name = "order/pay.html"
    model = Order
    pk_url_kwarg = "pk"
    context_object_name = "order"

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(user=self.request.user)


class SaveOrder(View):
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

            error_msg_stock = ""

            if stock < qtt_cart:
                cart[variation_id]["quantity"] = stock
                cart[variation_id]["quantitative_price"] = (
                    stock * unitary_price
                )
                cart[variation_id]["quantitative_promotional_price"] = (
                    stock * unitary_promotional_price
                )

                error_msg_stock = (
                    "Estoque insuficiente, valores corrigidos, "
                    "verifique seu carrinho."
                )

            if error_msg_stock:
                messages.error(self.request, error_msg_stock)
                self.request.session.save()
                return redirect("product:cart")

        qtt_total_cart = format.cart_total_qtt(cart)
        total_cart_value = format.cart_total(cart)

        order = Order(
            user=self.request.user,
            qtt_total=qtt_total_cart,
            total=total_cart_value,
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
                    price=variation["quantitative_price"],
                    price_promotional=variation[
                        "quantitative_promotional_price"
                    ],
                    quantity=variation["quantity"],
                    image=variation["image"],
                )
                for variation in cart.values()
            ]
        )

        del self.request.session["cart"]

        return redirect(reverse("order:pay", kwargs={"pk": order.pk}))


class Detail(View):
    pass


class List(View):
    pass
