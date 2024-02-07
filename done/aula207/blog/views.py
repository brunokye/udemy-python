from typing import Any
from django.shortcuts import render
from django.http import Http404
from blog.data import posts


def blog(request):
    context = {
        "text": "Blog",
        "title": "Blog",
        "posts": posts,
    }

    return render(request, "blog/index.html", context)


def post(request, id):
    found_post: dict[str, Any] | None = None

    for post in posts:
        if post["id"] == id:
            found_post = post
            break

    if found_post is None:
        raise Http404("Post não existe.")

    context = {"post": found_post, "title": found_post["title"]}

    return render(request, "blog/post.html", context)


def exemplo(request):
    context = {"text": "Exemplo", "title": "Exemplo"}
    return render(request, "blog/exemplo.html", context)
