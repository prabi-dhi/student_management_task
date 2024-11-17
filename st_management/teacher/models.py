from django.db import models
from classroom.models import Classroom

class Teacher(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.TextField(max_length = 50)
    department = models.TextField(max_length = 50)
    class_assigned = models.OneToOneField(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    