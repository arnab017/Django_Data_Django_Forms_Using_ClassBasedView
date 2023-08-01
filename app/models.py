from django.db import models

# Create your models here.

class Student(models.Model):
    sid = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=20)
    sage = models.IntegerField()
    
    def __str__(self):
        return self.sname
