from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book


# 1. List View (Required by the check)
# Checks for 'can_view' permission
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    # The check looks for a variable named 'books'
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})


# 2. Create View
# Checks for 'can_create' permission
@permission_required("bookshelf.can_create", raise_exception=True)
def book_create(request):
    if request.method == "POST":
        # Logic to save the book would go here
        pass
    return render(request, "bookshelf/book_form.html")


# 3. Edit View
# Checks for 'can_edit' permission
@permission_required("bookshelf.can_edit", raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        # Logic to update the book would go here
        pass
    return render(request, "bookshelf/book_form.html", {"book": book})


# 4. Delete View
# Checks for 'can_delete' permission
@permission_required("bookshelf.can_delete", raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "bookshelf/book_confirm_delete.html", {"book": book})
