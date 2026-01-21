from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Stores a single about me post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_on"]

    def __str__(self):
        return self.title
