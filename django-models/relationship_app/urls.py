from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView  # For class-based login/logout views

urlpatterns = [
    # Function-based views for register, login, and logout
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Optional: Class-based views for login/logout
    # path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]
