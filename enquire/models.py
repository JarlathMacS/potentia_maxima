from django.db import models
from django.utils import timezone


class FreeConsultationRequest(models.Model):
    """
    Stores a single free consultation request message
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["read", "-created_on"]

    def __str__(self):
        return f"Free consultation request from {self.name.title()}"
