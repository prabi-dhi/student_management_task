from django.db import models
from classroom.models import Classroom


class Student(models.Model):
    class Meta:
        db_table = 'student'
    s_id = models.CharField(max_length=10, primary_key=True)
    s_name = models.TextField(max_length = 50)
    class_enrolled = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    s_age = models.CharField(max_length = 3)
    is_deleted = models.BooleanField(default=False)


    def __str__(self):
        return self.s_name
    