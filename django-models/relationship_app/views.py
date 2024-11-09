from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test

# Custom check function to ensure the user has the 'Admin' role
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Admin view restricted to users with the 'Admin' role
@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome to the Admin view!")
