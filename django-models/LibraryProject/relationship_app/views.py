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

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def is_admin(user):
    return user.groups.filter(name='Admin').exists()

# Decorated view that only 'Admin' users can access
@user_passes_test(is_admin, login_url='/login/')
def admin_only_view(request):
    return render(request, 'admin_page.html')

# Check function to validate if the user is an admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

# Check function to validate if the user is a librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

# Check function to validate if the user is a member
def is_member(user):
    return user.userprofile.role == 'Member'

# Custom function to check user roles
def role_check(user, role):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == role

@user_passes_test(lambda user: role_check(user, 'Admin'))
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(lambda user: role_check(user, 'Librarian'))
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(lambda user: role_check(user, 'Member'))
def member_view(request):
    return render(request, 'member_view.html')
    
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

