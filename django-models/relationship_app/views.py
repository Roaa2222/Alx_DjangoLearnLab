from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm  # Only UserCreationForm is used here
from django.contrib.auth.models import User
from django.http import HttpResponse

# View for user registration
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect to a page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view without AuthenticationForm
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list_books')  # Redirect after login
        else:
            return HttpResponse("Invalid username or password")  # Simple response for invalid login
    return render(request, 'relationship_app/login.html')

# Logout view
def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')
