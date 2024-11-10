# relationship_app/views.py
from django.views.generic import DetailView
from .models import Library  # Ensure Library model is imported

# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Ensure correct template path
    context_object_name = 'library'  # Ensure context name is 'library'
