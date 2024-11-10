# relationship_app/views.py
from django.shortcuts import render
from .models import Book  # Ensure Book model is imported

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # This ensures all books are fetched
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Ensure the correct template path
