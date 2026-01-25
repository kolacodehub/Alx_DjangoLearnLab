from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # 'fieldsets' controls the layout when EDITING an existing user.
    # We append a new section called 'Custom Fields' with your new fields.
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("date_of_birth", "profile_photo")}),
    )

    # 'add_fieldsets' controls the layout when CREATING a new user.
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )


# Register the model with the new admin class
admin.site.register(CustomUser, CustomUserAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ("title", "author")
    list_filter = ("publication_year", "author")


admin.site.register(Book, BookAdmin)
