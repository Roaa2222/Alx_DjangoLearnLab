# relationship_app/views.py
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Import Library model

# Function-based view (FBV) to list all books
def list_books(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    # Render the 'list_books.html' template with the books context
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view (CBV) to display details of a specific library
class LibraryDetailView(DetailView):
    # The model associated with this view (Library)
    model = Library
    # The template to render for this view
    template_name = 'relationship_app/library_detail.html'
    # The name for the context variable that will be passed to the template
    context_object_name = 'library'
