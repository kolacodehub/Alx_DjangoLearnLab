from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    # This creates the beautiful two-column UI for the ManyToMany field
    filter_horizontal = ("following", "user_permissions", "groups")

    # We must add our custom fields to the layout so they actually appear on the page
    fieldsets = UserAdmin.fieldsets + (
        ("Profile & Social", {"fields": ("bio", "profile_picture", "following")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
