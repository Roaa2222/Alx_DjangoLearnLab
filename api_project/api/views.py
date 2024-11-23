from rest_framework.generics.ListAPIView import ListAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Fetch all books
    serializer_class = BookSerializer  # Use the serializer for the Book model
class BookViewSet(ModelViewSet):
    """
    A viewset for viewing, editing, creating, and deleting Book instances.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
