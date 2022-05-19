from django.db import models


class School(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=120)
    roll = models.IntegerField()

    def __str__(self):
        return self.name
