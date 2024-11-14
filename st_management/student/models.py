from django.db import models
from classroom.models import Classroom
# from django.contrib.auth.models import User

# from user.models import User

class Student(models.Model):
    s_id = models.CharField(max_length=10, primary_key=True)
    s_name = models.TextField(max_length = 50)
    class_enrolled = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    s_age = models.CharField(max_length = 3)
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return self.s_name