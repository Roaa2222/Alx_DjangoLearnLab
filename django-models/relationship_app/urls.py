from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # Ensure this imports your custom views from views.py

urlpatterns = [
    # URL pattern for the registration view
    path('register/', views.register, name='register'),

    # URL pattern for the login view with a custom template
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    # URL pattern for the logout view with a custom template (if applicable)
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
