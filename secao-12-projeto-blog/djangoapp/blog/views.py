from django.core.paginator import Paginator
from django.shortcuts import render
from django.db.models import Q
from blog.models import Post


PER_PAGE = 9


def index(request):
    posts = Post.objects.get_published()  # type: ignore
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
        },
    )


def created_by(request, author_id):
    posts = Post.objects.get_published().filter(  # type: ignore
        created_by__id=author_id
    )
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
        },
    )


def category(request, slug):
    posts = Post.objects.get_published().filter(  # type: ignore
        category__slug=slug
    )
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
        },
    )


def page(request, slug):
    return render(request, "blog/pages/page.html")


def post(request, slug):
    post = (
        Post.objects.get_published().filter(slug=slug).first()  # type: ignore
    )

    return render(request, "blog/pages/post.html", {"post": post})


def tag(request, slug):
    posts = Post.objects.get_published().filter(tag__slug=slug)  # type: ignore
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
        },
    )


def search(request):
    search_value = request.GET.get("search", "").strip()

    posts = Post.objects.get_published().filter(  # type: ignore
        Q(title__icontains=search_value)
        | Q(excerpt__icontains=search_value)
        | Q(content__icontains=search_value)
    )[:PER_PAGE]

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": posts,
            "search_value": search_value,
        },
    )
