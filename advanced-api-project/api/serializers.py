from rest_framework import serializers
from .models import Author, Book
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    """
    Handles the conversion of Book model instances into JSON format.

    Purpose: To provide a complete representation of a Book, including
    validation logic to ensure data integrity during creation or updates.
    """

    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value):
        """
        Custom validator for the publication_year field.
        Ensures that books cannot be registered with a year that hasn't happened yet.
        """
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Handles the conversion of Author model instances into JSON format.

    Purpose: To represent an Author and, importantly, to provide a
    nested view of all books associated with that Author.
    """

    # Relationship Handling:
    # This field explicitly tells DRF to use the BookSerializer to represent
    # the 'books' related_name defined in the Book model.
    # 'many=True' is required because one author can have multiple books.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]
