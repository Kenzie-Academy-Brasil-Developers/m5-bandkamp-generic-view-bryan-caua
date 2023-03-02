from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(unique=True, error_messages={"unique":"A user with that username already exists."}, max_length=100)
    email = models.CharField(unique=True, error_messages={"unique":"This field must be unique."}, max_length=100)