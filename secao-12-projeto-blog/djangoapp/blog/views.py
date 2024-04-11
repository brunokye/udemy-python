from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import Http404, HttpRequest
from blog.models import Post, Page


PER_PAGE = 9


class PostListView(ListView):
    template_name = "blog/pages/index.html"
    context_object_name = "posts"
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


# def index(request):
#     posts = Post.objects.get_published()  # type: ignore
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)


#     return render(
#         request,
#         "blog/pages/index.html",
#         {"page_obj": page_obj, "page_title": "Home"},
#     )


class CreatedByListView(PostListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_id = self.kwargs.get("author_id")
        user = User.objects.filter(pk=author_id).first()

        if user is None:
            raise Http404()

        user_full_name = user.username
        if user.first_name:
            user_full_name = f"{user.first_name} {user.last_name}"

        page_title = f"Posts de {user_full_name}"
        context.update({"page_title": page_title})
        context["user"] = user

        return context

    def get_queryset(self):
        qs = super().get_queryset()
        author_id = self.kwargs.get("author_id")
        qs = qs.filter(created_by__pk=author_id)
        return qs


# def created_by(request, author_id):
#     user = User.objects.filter(pk=author_id).first()

#     if user is None:
#         raise Http404()

#     user_full_name = user.username

#     if user.first_name:
#         user_full_name = f"{user.first_name} {user.last_name}"

#     page_title = f"Posts de {user_full_name}"
#     posts = Post.objects.get_published().filter(  # type: ignore
#         created_by__id=author_id
#     )
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     return render(
#         request,
#         "blog/pages/index.html",
#         {
#             "page_obj": page_obj,
#             "page_title": page_title,
#         },
#     )


class CategoryListView(PostListView):
    allow_empty = False

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(category__slug=self.kwargs.get("slug"))
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_title = (
            f"Categoria {self.object_list[0].category.name}"  # type: ignore
        )
        context.update({"page_title": page_title})
        return context


# def category(request, slug):
#     posts = Post.objects.get_published().filter(  # type: ignore
#         category__slug=slug
#     )

#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     if len(page_obj) == 0:
#         raise Http404()

#     page_title = f"Categoria {page_obj[0].category.name}"

#     return render(
#         request,
#         "blog/pages/index.html",
#         {
#             "page_obj": page_obj,
#             "page_title": page_title,
#         },
#     )


class TagListView(PostListView):
    allow_empty = False

    def get_queryset(self):
        return super().get_queryset().filter(tag__slug=self.kwargs.get("slug"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_title = (
            f"Tag {self.object_list[0].tag.first().name}"  # type: ignore
        )
        context.update({"page_title": page_title})
        return context


# def tag(request, slug):
#     posts = (
#         Post.objects.get_published().filter(tag__slug=slug)  # type: ignore
#     )
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     if len(page_obj) == 0:
#         raise Http404()

#     page_title = f"Tag {page_obj[0].tag.first().name}"

#     return render(
#         request,
#         "blog/pages/index.html",
#         {
#             "page_obj": page_obj,
#             "page_title": page_title,
#         },
#     )


class SearchListView(PostListView):
    def __init__(self, *args, **kwargs):
        self.search_value = ""
        super().__init__(*args, **kwargs)

    def setup(self, request: HttpRequest, *args, **kwargs):
        self.search_value = request.GET.get("search", "").strip()
        return super().setup(request, *args, **kwargs)

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                Q(title__icontains=self.search_value)
                | Q(excerpt__icontains=self.search_value)
                | Q(content__icontains=self.search_value)
            )[:PER_PAGE]
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page_title = f"Search {self.search_value[:10]}"
        context.update(
            {"page_title": page_title, "search_value": self.search_value}
        )
        return context

    def get(self, request, *args, **kwargs):
        if self.search_value == "":
            return redirect("blog:index")
        return super().get(request, *args, **kwargs)


# def search(request):
#     search_value = request.GET.get("search", "").strip()

#     posts = Post.objects.get_published().filter(  # type: ignore
#         Q(title__icontains=search_value)
#         | Q(excerpt__icontains=search_value)
#         | Q(content__icontains=search_value)
#     )[:PER_PAGE]

#     page_title = f"Search {search_value[:10]}"

#     return render(
#         request,
#         "blog/pages/index.html",
#         {
#             "page_obj": posts,
#             "search_value": search_value,
#             "page_title": page_title,
#         },
#     )


class PageDetailView(DetailView):
    model = Page
    template_name = "blog/pages/page.html"
    slug_field = "slug"
    context_object_name = "page"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.get_object()
        context.update({"page_title": page.title})  # type: ignore
        return context

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


# def page(request, slug):
#     page = Page.objects.filter(is_published=True).filter(slug=slug).first()

#     if page is None:
#         raise Http404()

#     return render(
#         request,
#         "blog/pages/page.html",
#         {
#             "page": page,
#             "page_title": page.title,
#         },
#     )


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
