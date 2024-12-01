# api/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters 

class BookListView(generics.ListAPIView):
    """
    List all books with advanced query capabilities: filtering, searching, and ordering.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Add filtering, searching, and ordering capabilities
    filter_backends = [
        DjangoFilterBackend,  # For filtering
        filters.SearchFilter,  # For searching
        filters.OrderingFilter  # For ordering
         DjangoFilterBackend, 
    ]

    # Define filterable fields
    filterset_fields = ['title', 'author', 'published_date', 'publication_year']

    # Define searchable fields
    search_fields = ['title', 'author']

    # Define ordering fields
    ordering_fields = ['title', 'published_date']
    
# List view: Read-only access for all users
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Detail view: Read-only access for all users
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Create view: Only authenticated users can create
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Update view: Only authenticated users can update
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Delete view: Only authenticated users can delete
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

