from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .forms import PostForm, AuthorForm
from .models import Post, Author


# Create your views here.
def post(request):
    t = loader.get_template("posts/main.html")
    return HttpResponse(t.render())


def posts_list(request):
    if request.method == "POST":
        form = PostForm(data=request.POST)

        if form.is_valid():
            Post.objects.get_or_create(**form.cleaned_data)
            messages.add_message(request, messages.SUCCESS, "Utworzono nowy Post!!")
        else:
            messages.add_message(request, messages.ERROR, form.errors.get("__all__"))

    form = PostForm()
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/posts_list.html",
        context={"posts": posts, "form": form},
    )


def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(
        request=request, template_name="posts/post_details.html", context={"post": post}
    )


def authors_list(request):
    if request.method == "POST":
        form = AuthorForm(data=request.POST)

        if form.is_valid():
            Author.objects.get_or_create(**form.cleaned_data)
            messages.add_message(request, messages.SUCCESS, "Utworzono nowego Autora!!")
        else:
            messages.add_message(request, messages.ERROR, form.errors.get("__all__"))

    form = AuthorForm()
    authors = Author.objects.all()
    return render(
        request=request,
        template_name="posts/authors_list.html",
        context={"authors": authors, "form": form},
    )


def author_details(request, id):
    author = Author.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/author_details.html",
        context={"author": author},
    )
