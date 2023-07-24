from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.
class CustomUser(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_officer = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    email = models.EmailField(unique=True)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']   