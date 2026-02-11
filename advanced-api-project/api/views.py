from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    PURPOSE: Provides a read-only list of all books in the database.
    PERMISSIONS: AllowAny - Publicly accessible for catalog browsing.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


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
