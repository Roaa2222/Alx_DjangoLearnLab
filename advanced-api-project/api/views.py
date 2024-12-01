# api/views.py

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    Handles retrieving a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Publicly accessible


class BookDetailView(generics.RetrieveAPIView):
    """
    Handles retrieving a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Publicly accessible


class BookCreateView(generics.CreateAPIView):
    """
    Handles creating a new book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requires login


class BookUpdateView(generics.UpdateAPIView):
    """
    Handles updating an existing book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requires login


class BookDeleteView(generics.DestroyAPIView):
    """
    Handles deleting a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Requires login
