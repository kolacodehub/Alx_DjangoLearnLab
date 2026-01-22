from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile


# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    search_fields = ("title",)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ("books",)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(UserProfile)
