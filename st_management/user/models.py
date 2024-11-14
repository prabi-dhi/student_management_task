from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     id = models.CharField(max_length=100, primary_key=True)
#     password = models.CharField(max_length=30)
#     last_login = models.CharField(max_length=100)
#     is_superuser = models.CharField(max_length=100)
#     username = models.CharField(max_length=100, unique=True)
#     email = models.CharField(max_length=100)
#     is_staff = models.CharField(max_length=100)
#     is_active = models.CharField(max_length=100)
#     date_joined = models.CharField(max_length=100)

