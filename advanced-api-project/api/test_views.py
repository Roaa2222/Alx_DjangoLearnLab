from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for authenticated tests
        cls.user = User.objects.create_user(username="testuser", password="password123")
        
        # Create sample books
        cls.book1 = Book.objects.create(
            title="Book One",
            author="Author One",
            published_date="2022-01-01",
            isbn="1234567890123"
        )
        cls.book2 = Book.objects.create(
            title="Book Two",
            author="Author Two",
            published_date="2023-01-01",
            isbn="1234567890124"
        )
        
        # APIClient for authenticated requests
        cls.authenticated_client = APIClient()
        cls.authenticated_client.login(username="testuser", password="password123")
    
    def test_list_books(self):
        # Test retrieving all books
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_filter_books_by_title(self):
        # Test filtering books by title
        url = reverse("book-list") + "?title=Book One"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_search_books_by_author(self):
        # Test searching books by author
        url = reverse("book-list") + "?search=Author Two"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Author Two")

    def test_order_books_by_published_date(self):
        # Test ordering books by published date
        url = reverse("book-list") + "?ordering=published_date"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_create_book_authenticated(self):
        # Test creating a book with authenticated user
        url = reverse("book-create")
        data = {
            "title": "Book Three",
            "author": "Author Three",
            "published_date": "2023-06-01",
            "isbn": "1234567890125"
        }
        response = self.authenticated_client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_authenticated(self):
        # Test updating a book with authenticated user
        url = reverse("book-update", kwargs={"pk": self.book1.id})
        data = {"title": "Updated Book One"}
        response = self.authenticated_client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_delete_book_authenticated(self):
        # Test deleting a book with authenticated user
        url = reverse("book-delete", kwargs={"pk": self.book2.id})
        response = self.authenticated_client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_create_book_unauthenticated(self):
        # Test creating a book without authentication
        url = reverse("book-create")
        data = {
            "title": "Book Four",
            "author": "Author Four",
            "published_date": "2023-06-01",
            "isbn": "1234567890126"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
