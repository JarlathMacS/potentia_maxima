from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# CONSTANT for CoachingPost model
STATUS = ((0, "Draft"), (1, "Published"))


class CoachingPost(models.Model):
    """
    Stores a single coaching post entry related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)

    class Meta:
        ordering = ["-updated_on"]

    def __str__(self):
        return f"{self.title} | by Coach {self.author.title()}"


class ProgressComment(models.Model):
    """
    Stores a single progress comment entry related to :model:`auth.User`
    and :model:`home.CoachingPost`.
    """
    post = models.ForeignKey(
        CoachingPost,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="commenter",
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-updated_on"]

    def __str__(self):
        return (
            f"Progress comment by {self.author.title()} | "
            f"on coaching post {self.post.title}"
        )
