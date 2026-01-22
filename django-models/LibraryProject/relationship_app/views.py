from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from .models import Book
from .models import Library


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


# 1. Helper functions to check roles
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == "Admin"

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == "Librarian"

def is_member(user):
    return user.is_authenticated and user.userprofile.role == "Member"

# 2. Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")

@user_passes_test(is_member)
def member_view(request):
    return render(request, "relationship_app/member_view.html")

# Authentication
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
