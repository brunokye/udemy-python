from django.urls import path
from .views import Create, Login, Logout

app_name = "profile"

urlpatterns = [
    path("", Create.as_view(), name="create"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
]
