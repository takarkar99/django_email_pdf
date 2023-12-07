from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomManager
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email_address"), max_length=250, unique=True)
    is_active = models.BooleanField(default=False)
    email_is_verified = models.BooleanField(default=False)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomManager()


    def __str__(self):
        return self.email