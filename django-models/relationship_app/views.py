from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == UserProfile.Role.ADMIN

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == UserProfile.Role.LIBRARIAN

def admin_view(request):
    # Your admin view logic here
    return render(request, 'admin_view.html')

@user_passes_test(is_admin)
def librarian_view(request):
    # Your librarian view logic here
    return render(request, 'librarian_view.html')

@user_passes_test(is_librarian)
def member_view(request):
    # Your member view logic here
    return render(request, 'member_view.html')
