from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"

    # Add this method to load signals
    def ready(self):
        import blog.signals
