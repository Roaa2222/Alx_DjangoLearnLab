from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Author
from django.db import models
from .models import Library  

class ExampleModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        permissions = [
            ('can_view_example', 'Can view example'),  # Custom permission
            ('can_edit_example', 'Can edit example'),  # Additional permission if needed
        ]

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title
class Librarian(models.Model):
    name = models.CharField(max_length=255)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name="librarian")

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    # Define the role choices with only Admin and Member
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member')
    ]

    # One-to-One relationship with the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Role field with predefined choices: Admin and Member
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

# Signal to create or update the UserProfile when a User is created or saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()

