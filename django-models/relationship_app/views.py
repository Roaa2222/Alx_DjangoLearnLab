from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Library  # Ensure this import is present

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Ensure you have this template
    context_object_name = 'library'

    # Optionally, if you want to customize the context:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Fetch all books associated with the library
        return context
