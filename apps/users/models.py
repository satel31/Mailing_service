from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(verbose_name='Email', unique=True)

    activation_code = models.CharField(max_length=50, verbose_name='activation code', **NULLABLE)
    is_activated = models.BooleanField(default=False, verbose_name='activated')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
