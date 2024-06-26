from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário registrado com sucesso.")
            return redirect("contact:login")

    return render(request, "contact/register.html", {"form": form})


def login(request):
    form = AuthenticationForm(request)

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, "Login realizado com sucesso.")
            return redirect("contact:index")

    return render(request, "contact/login.html", {"form": form})


@login_required(login_url="contact:login")
def update_user(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method == "POST":
        form = RegisterUpdateForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário atualizado com sucesso.")
            return redirect("contact:update_user")

    return render(request, "contact/update.html", {"form": form})


@login_required(login_url="contact:login")
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout realizado com sucesso.")
    return redirect("contact:login")
