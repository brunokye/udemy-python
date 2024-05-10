from django.urls import path
from .views import Pay, SaveOrder, Detail, List

app_name = "order"

urlpatterns = [
    path("pay/<int:pk>", Pay.as_view(), name="pay"),
    path("saveorder/", SaveOrder.as_view(), name="saveorder"),
    path("list/", List.as_view(), name="list"),
    path("detail/<int:pk>", Detail.as_view(), name="detail"),
]
