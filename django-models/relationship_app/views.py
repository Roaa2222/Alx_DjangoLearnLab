# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Ensure Library is imported here

# Function-based view (FBV) to list all books
def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    # Render the 'list_books.html' template with the books context
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view (CBV) to display details of a specific library
class LibraryDetailView(DetailView):
    model = Library  # This will use the Library model to fetch details
    template_name = 'relationship_app/library_detail.html'  # Path to the template
    context_object_name = 'library'  # The name of the context variable for the template
