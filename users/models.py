from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtendUser(AbstractUser):
    email = models.EmailField(blank=False, verbose_name='email', max_length=255)
    USERNAME_FIELD = 'username'
    EAMIL_FIELD = 'email'


