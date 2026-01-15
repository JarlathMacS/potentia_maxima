from django.db import models

# Create your models here.


class FreeConsultationRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(
        max_length=200, unique=True, blank=False, null=False
    )
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Free consultation request from {self.name}"
