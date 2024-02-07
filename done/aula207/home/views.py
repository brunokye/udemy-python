from django.shortcuts import render


def home(request):
    context = {"text": "Home", "title": "Home"}
    return render(request, "home/index.html", context)
