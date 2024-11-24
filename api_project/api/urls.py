from django.urls import path,include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Route to BookList view
    path('', include(router.urls)),
]