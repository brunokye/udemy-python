from django.urls import path
from .views import (
    ProductList,
    ProductDetail,
    ProductAddItem,
    ProductRemoveItem,
    ProductCart,
    ProductCheckout,
)

app_name = "product"

urlpatterns = [
    path("", ProductList.as_view(), name="list"),
    path("<slug>", ProductDetail.as_view(), name="detail"),
    path("additem/", ProductAddItem.as_view(), name="additem"),
    path("removeitem/", ProductRemoveItem.as_view(), name="removeitem"),
    path("cart/", ProductCart.as_view(), name="cart"),
    path("checkout/", ProductCheckout.as_view(), name="checkout"),
]
