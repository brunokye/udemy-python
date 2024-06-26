from django.urls import path
from contact import views

app_name = "contact"

urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("contact/create", views.create, name="create"),
    path("contact/<int:contact_id>/detail/", views.detail, name="detail"),
    path(
        "contact/<int:contact_id>/update/",
        views.update_contact,
        name="update_contact",
    ),
    path("contact/<int:contact_id>/delete/", views.delete, name="delete"),
    path("user/register", views.register, name="register"),
    path("user/login", views.login, name="login"),
    path("user/update", views.update_user, name="update_user"),
    path("user/logout", views.logout, name="logout"),
]
