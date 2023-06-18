from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Class represents Profile model, related one to one with
    User model. 
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)
    bio = models.TextField(max_length=150, blank=True)
    equipment = models.TextField(max_length=70, blank=True)
    instagram = models.CharField(max_length=70, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=255, blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_nsvhkq'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Profile is created automatically when new user is registered.
    """
    if created:
        Profile.objects.create(owner=instance)

post_save.connect(create_profile, sender=User)