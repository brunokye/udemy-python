from django.urls import path
from .views import Pay, Checkout, Detail

app_name = "order"

urlpatterns = [
    path("", Pay.as_view(), name="pay"),
    path("checkout/", Checkout.as_view(), name="checkout"),
    path("detail/", Detail.as_view(), name="detail"),
]
