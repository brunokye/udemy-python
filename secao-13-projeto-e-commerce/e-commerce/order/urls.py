from django.urls import path
from .views import Pay, SaveOrder, Detail

app_name = "order"

urlpatterns = [
    path("", Pay.as_view(), name="pay"),
    path("saveorder/", SaveOrder.as_view(), name="saveorder"),
    path("detail/", Detail.as_view(), name="detail"),
]
