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
    category = models.CharField(choices=POST_CATEGORIES, max_length=20)
    tags = models.CharField(max_length=100)
    exif = models.CharField(max_length=150)
    body = models.TextField(max_length=300)
    # set image placeholder if user don't provide image
    image = models.ImageField(
        upload_to='images/', 
        default='../default_post_hc3mjm',
        blank=True
    )
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
