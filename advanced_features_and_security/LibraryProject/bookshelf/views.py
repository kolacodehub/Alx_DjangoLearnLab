from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Article


# 1. View checking 'can_view'
@permission_required("users.can_view", raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, "articles/article_list.html", {"articles": articles})


# 2. View checking 'can_create'
@permission_required("users.can_create", raise_exception=True)
def article_create(request):
    if request.method == "POST":
        # Logic to save article would go here
        pass
    return render(request, "articles/article_form.html")


# 3. View checking 'can_edit'
@permission_required("users.can_edit", raise_exception=True)
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        # Logic to update article would go here
        pass
    return render(request, "articles/article_form.html", {"article": article})


# 4. View checking 'can_delete'
@permission_required("users.can_delete", raise_exception=True)
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect("article_list")
    return render(request, "articles/article_confirm_delete.html", {"article": article})
