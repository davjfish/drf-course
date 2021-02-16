from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=240, blank=True, null=True)
    city = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.username


class ProfileStatus(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="statuses")
    status_content = models.CharField(max_length=240, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_profile

    class Meta:
        verbose_name_plural = "profile statuses"


