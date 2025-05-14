# backend/users/models.py
# Define Profile model that extends the built-in User model through a one-to-one relationship

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    Profile model that extends the built-in Django User model.
    Automatically created/updated when User instances are created/updated.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    
    def __str__(self):
        return f'{self.user.username} Profile'

# Signal to create/update Profile when User is created/updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create or update a user profile when a user is created or updated.
    """
    if created:
        Profile.objects.create(user=instance)
    else:
        # Make sure profile exists even if user was created before this code
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()