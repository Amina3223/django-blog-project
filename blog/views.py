"""
Vistes de l'aplicació blog.
"""

from django.shortcuts import render, get_object_or_404
from .models import Post, Author, Tag


def starting_page(request):
    """
    Mostra els 3 darrers posts.
    """
    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    """
    Mostra tots els posts.
    """
    all_posts = Post.objects.all().order_by("-date")

    return render(request, "blog/post_list.html", {
        "posts": all_posts
    })


def post_detail(request, id):
    """
    Mostra un post individual.
    """
    post = get_object_or_404(Post, id=id)

    return render(request, "blog/post_detail.html", {
        "post": post
    })


def authors(request):
    """
    Mostra tots els autors.
    """
    all_authors = Author.objects.all()

    return render(request, "blog/authors_list.html", {
        "authors": all_authors
    })


def author_detail(request, author_id):
    """
    Mostra detall d'un autor.
    """
    author = get_object_or_404(Author, id=author_id)

    return render(request, "blog/author_detail.html", {
        "author": author
    })


def tags(request):
    """
    Mostra totes les tags.
    """
    all_tags = Tag.objects.all()

    return render(request, "blog/tag_list.html", {
        "tags": all_tags
    })


def tag_posts(request, tag):
    """
    Mostra posts filtrats per tag.
    """
    selected_tag = get_object_or_404(Tag, tag=tag)

    tagged_posts = Post.objects.filter(tags=selected_tag)

    return render(request, "blog/tag_posts.html", {
        "tag": selected_tag,
        "posts": tagged_posts
    })




def custom_404(request, exception):
    return render(request, "blog/404.html", status=404)