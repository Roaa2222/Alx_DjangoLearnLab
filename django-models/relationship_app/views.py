from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Library  # Ensure both imports are present
from django.contrib.auth import login

# Function-based view to list all books and their authors
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # Import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            messages.success(request, "Your account has been created successfully!")  # Add a success message
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserCreationForm()  # Instantiate the form for GET request
    
    return render(request, 'relationship_app/register.html', {'form': form})  # Ensure the template is correct


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

