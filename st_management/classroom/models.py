from django.db import models

class Classroom(models.Model):
    room_number = models.CharField(max_length=10, primary_key=True)
    total_student = models.CharField(max_length = 5)     
    
    def __str__(self):
        return self.room_number
    
