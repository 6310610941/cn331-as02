from django.db import models

# Create your models here.

from courses.models import Course

class Student(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    subject = models.ManyToManyField(Course, blank=True, related_name='Student')

    def __str__(self):
        return f"{ self.first }  { self.last }"