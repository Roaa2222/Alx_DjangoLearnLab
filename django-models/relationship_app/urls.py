from django.urls import path
from . import views

urlpatterns = [
    # URL for function-based view
    path('books/', views.list_books, name='list_books'),
    
    # URL for class-based view
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
