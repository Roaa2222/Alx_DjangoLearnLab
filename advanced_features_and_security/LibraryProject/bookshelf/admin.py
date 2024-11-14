from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Define the fields to display in the admin panel
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth']
    search_fields = ['email', 'username']

# Register the CustomUser with the custom admin class
admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in the admin list view
    search_fields = ('title', 'author')  # Enable search functionality
    list_filter = ('publication_year',)  # Add filter options for the publication year
