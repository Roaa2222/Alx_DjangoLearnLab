from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library  # Ensure both imports are present

# Function-based view to list all books and their authors
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Template for library details
    context_object_name = 'library'

    # Optionally, customize the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Fetch all books related to the library
        return context
