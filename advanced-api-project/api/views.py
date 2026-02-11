from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters import rest_framework

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    View to list all books.

    Capabilities:
    - Filtering: precise matches on title, author, and publication_year.
    - Searching: fuzzy matches on title and author name.
    - Ordering: sort results by title and publication_year.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # CONFIGURATION:
    # 1. DjangoFilterBackend: Handle simple equality-based filtering
    # 2. SearchFilter: Handle keyword text search
    # 3. OrderingFilter: Handle sorting of results
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # FILTERS:
    # Use 'filterset_fields' for exact matches.
    # Example: ?author=1 (Returns books by Author ID 1)
    filterset_fields = ["title", "author", "publication_year"]

    # SEARCH:
    # Use 'search_fields' for text search.
    # Note: 'author__name' allows searching by the related author's text name, not just ID.
    search_fields = ["title", "author__name"]

    # ORDERING:
    # Use 'ordering_fields' to allow client-controlled sorting.
    # Default ordering is usually by ID, but clients can override this
    ordering_fields = ["title", "publication_year"]


class BookDetailView(generics.RetrieveAPIView):
    """
    PURPOSE: Retrieves full details of a single book using its ID (pk).
    PERMISSIONS: AllowAny - Publicly accessible.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    PURPOSE: Allows creation of new book entries.
    PERMISSIONS: IsAuthenticated - Only logged-in users can contribute.
    HOOKS: perform_create is used to handle logic before saving.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Custom hook: Logic can be added here (e.g., logging or setting user)
        serializer.save()


class BookUpdateView(generics.RetrieveUpdateAPIView):
    """
    PURPOSE: Updates an existing book.
    NOTE: Uses RetrieveUpdateAPIView so the form pre-populates with existing data.
    PERMISSIONS: IsAuthenticated - Only logged-in users can edit.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    PURPOSE: Removes a book record from the system.
    PERMISSIONS: IsAuthenticated - Only logged-in users can delete.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
