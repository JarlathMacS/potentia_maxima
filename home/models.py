from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))

# class AllUsers(models.Model):


# class CoachingStaff(models.Model):
#     staff_id = models.IntegerField(primary_key=True)
#     user_id = models.OneToOneField(AllUsers, on_delete=models.CASCADE, related_name="tbd")
#     superuser = models.BooleanField()


# class Status(models.Model):
#     status_id = models.IntegerField(primary_key=True)
#     description = models.CharField(max_length=50, unique=True)


class CoachingPost(models.Model):
    """
    Stores a single coaching post entry related to :model:`auth.User`.
    """
    # post_id = models.IntegerField(primary_key=True)
    title = models.CharField(
        max_length=200, unique=True
    )
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # staff_id = models.ForeignKey(CoachingStaff, on_delete=models.CASCADE, related_name="tbd")
    status = models.IntegerField(choices=STATUS, default=0)
    # status_id = models.OneToOneField(Status, on_delete=models.CASCADE, related_name="tbd")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    # image = models.CharField(max_length=200)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


# class ClientUser(models.Model):
#     client_id = models.IntegerField(primary_key=True)
#     user_id = models.OneToOneField(AllUsers, on_delete=models.CASCADE, related_name="tbd")
#     active = models.BooleanField()

class ProgressComment(models.Model):
    """
    Stores a single progress comment entry related to :model:`auth.User`
    and :model:`home.CoachingPost`.
    """
    post = models.ForeignKey(CoachingPost, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Progress comment {self.body} by {self.author}"
