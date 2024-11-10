from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# View for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after successful registration
            return redirect('home')  # Replace 'home' with your desired redirect URL
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# You can add views for login and logout using Django’s built-in views or customize as needed.
