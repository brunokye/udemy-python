from django.urls import path
from .views import Create, Update, Login, Logout

app_name = "profile"

urlpatterns = [
    path("", Create.as_view(), name="create"),
    path("update/", Update.as_view(), name="update"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
]
