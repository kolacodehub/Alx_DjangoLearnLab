from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "truncated_content", "created_at")
    search_fields = ("title", "content")

    @admin.display(description="Content Preview")
    def truncated_content(self, obj):
        if len(obj.content) > 50:
            return f"{obj.content[:50]}..."
        return obj.content


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "post", "truncated_comment", "created_at")
    search_fields = ("content",)

    @admin.display(description="Comment Excerpt")
    def truncated_comment(self, obj):
        if len(obj.content) > 30:
            return f"{obj.content[:30]}..."
        return obj.content


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
