from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # This view stays public? Or maybe we lock it down too:
    # permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for Books.
    Permissions:
    - IsAuthenticated: Only logged-in users can access this.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Ensures only authorized users can access
