from django.db import models
from django.utils import timezone
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class Videos(models.Model):
    title = models.CharField(max_length=50)
    defenition = models.TextField(max_length=150, null=True)
    video = models.FileField(upload_to='video')

    def __str__(self):
        return self.title



class Exercises(models.Model):
    title = models.CharField(max_length=50, null=True)
    defenition = models.TextField(max_length=150, null=True)
    deadline = models.DateTimeField(auto_now=False)
    exercise = models.FileField(upload_to='exercise')

    def __str__(self):
        return self.title


class Responses(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='response')
    # student = models.CharField(max_length=50)
    # student_id = models.IntegerField(null=False)
    #score = models.FloatField(null=True)

    def __str__(self):
        return self.title


class Student_Login(models.Model):
    Email = models.EmailField(max_length=50, null=False, default="")
    student_id = models.IntegerField(default=False)
    password = models.CharField(max_length=20)


class Teacher_Login(models.Model):
    Email = models.EmailField(max_length=50, null=False, default="")
    password = models.CharField(max_length=20)


class Results(models.Model):
    student_number = models.DecimalField(max_digits=610399300, decimal_places=0, null=False)
    date = models.DateTimeField(auto_now=True)
    file = models.FileField()
    score = models.DecimalField(max_digits=100, decimal_places=2, null=True)


#class Student(models.Model):
 #   upload_response = models.FileField(upload_to='response')