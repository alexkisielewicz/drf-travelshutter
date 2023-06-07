from django.db import models
from django.contrib.auth.models import User
from .constants import POST_CATEGORIES

class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    category = models.CharField(choices=POST_CATEGORIES, max_length=20, default="travel")
    hashtags = models.CharField(max_length=100, blank=True)
    exif = models.CharField(max_length=150, blank=True)
    body = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', 
        default='../default_post_hc3mjm',
        blank=True
    )
    
    def format_hashtags(self, *args, **kwargs):
        # Split the input hashtags by commas and remove any leading/trailing spaces
        hashtags = [hashtag.strip() for hashtag in self.hashtags.split(',') if hashtag.strip()]
        super().save(*args, **kwargs)
        self.hashtags.set(hashtags)
        
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'