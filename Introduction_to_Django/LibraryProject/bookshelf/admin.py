from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in the admin list view
    search_fields = ('title', 'author')  # Enable search functionality
    list_filter = ('publication_year',)  # Add filter options for the publication year
