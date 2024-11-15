from django.contrib.auth.models import User
from django.db import models

class User(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class User(AbstractUser):
#     class Types(models.TextChoices):
#         TEACHER = "TEACHER", "Teacher"
#         STUDENT = "STUDENT", "Student"
#         ADMINISTRATION = "ADMINISTRATION", 

#     type = models.CharField(max_length=20, choices=Types.choices, default=Types.STUDENT)
#     email = models.EmailField(unique=True, max_length=50)
#     username = models.CharField(unique=True, max_length=20)

#     # USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username"]

#     def __str__(self):
#         return self.email

