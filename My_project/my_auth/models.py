from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    profile_picture = models.ImageField(
        upload_to="uploads/profile_pictures/", null=True, blank=True
    )
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.username)
