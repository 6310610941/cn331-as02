from django.db import models

# Create your models here.

class Course(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{ self.code } : { self.name } "

class Info(models.Model):
    subname = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="Subject_Name")
    semester = models.IntegerField()
    year = models.IntegerField()
    seat = models.IntegerField()
    status = models.CharField(max_length=64)

    def __str__(self):
        return f"{ self.id } : { self.semester }/{ self.year } : { self.seat }: { self.status }"
