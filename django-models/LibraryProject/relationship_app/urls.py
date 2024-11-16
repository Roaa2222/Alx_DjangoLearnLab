from django.urls import path
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),
]
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView  # Import Login and Logout views
from . import views  # Import the custom register view
from .views import admin_only_view



urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # Login URL pattern
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # Logout URL pattern
    path('register/', views.register, name='register'),  # Register URL pattern,
    path('admin-view/', admin_only_view, name='admin_only_view'), 
]
