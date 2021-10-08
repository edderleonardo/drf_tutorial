from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    total_fortune = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.email
