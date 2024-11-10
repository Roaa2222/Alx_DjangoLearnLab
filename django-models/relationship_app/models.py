from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    # Define the role choices with only Admin and Member
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Member', 'Member')
        ('Librarian', 'Librarian')
    ]

    # One-to-One relationship with the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Role field with predefined choices: Admin and Member
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

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
