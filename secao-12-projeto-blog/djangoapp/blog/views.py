from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.shortcuts import render
from django.db.models import Q
from django.http import Http404
from blog.models import Post, Page


PER_PAGE = 9


class PostListView(ListView):
    model = Post
    template_name = "blog/pages/index.html"
    context_object_name = "posts"
    ordering = ("-pk",)
    paginate_by = PER_PAGE
    queryset = Post.objects.get_published()  # type: ignore

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(is_published=True)
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"page_title": "Home"})
        return context


def index(request):
    posts = Post.objects.get_published()  # type: ignore
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "blog/pages/index.html",
        {"page_obj": page_obj, "page_title": "Home"},
    )


def created_by(request, author_id):
    user = User.objects.filter(pk=author_id).first()

    if user is None:
        raise Http404()

    user_full_name = user.username

    if user.first_name:
        user_full_name = f"{user.first_name} {user.last_name}"

    page_title = f"Posts de {user_full_name}"
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
            "page_title": page_title,
        },
    )


def category(request, slug):
    posts = Post.objects.get_published().filter(  # type: ignore
        category__slug=slug
    )

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()

    page_title = f"Categoria {page_obj[0].category.name}"

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
            "page_title": page_title,
        },
    )


def page(request, slug):
    page = Page.objects.filter(is_published=True).filter(slug=slug).first()

    if page is None:
        raise Http404()

    page_title = page.title

    return render(
        request,
        "blog/pages/page.html",
        {
            "page": page,
            "page_title": page_title,
        },
    )


def post(request, slug):
    post = (
        Post.objects.get_published().filter(slug=slug).first()  # type: ignore
    )

    if post is None:
        raise Http404()

    page_title = post.title

    return render(
        request,
        "blog/pages/post.html",
        {
            "post": post,
            "page_title": page_title,
        },
    )


def tag(request, slug):
    posts = Post.objects.get_published().filter(tag__slug=slug)  # type: ignore
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()

    page_title = f"Tag {page_obj[0].tag.first().name}"

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": page_obj,
            "page_title": page_title,
        },
    )


def search(request):
    search_value = request.GET.get("search", "").strip()

    posts = Post.objects.get_published().filter(  # type: ignore
        Q(title__icontains=search_value)
        | Q(excerpt__icontains=search_value)
        | Q(content__icontains=search_value)
    )[:PER_PAGE]

    page_title = f"Search {search_value[:10]}"

    return render(
        request,
        "blog/pages/index.html",
        {
            "page_obj": posts,
            "search_value": search_value,
            "page_title": page_title,
        },
    )
