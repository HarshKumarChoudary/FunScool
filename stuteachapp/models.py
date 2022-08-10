from django.db import models
from django.contrib.auth.models import User

#Student models

class student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=20)
    rollno = models.IntegerField()
    standard = models.IntegerField()
    stream = models.CharField(max_length=40)

#teacher models

class teacher(models.Model):
    category_list = [
        ('Physics','Physics'),
        ('Chemistry','Chemistry'),
        ('Social Science','Social Science'),
        ('Mathematics','Mathematics'),
        ('Biology','Biology'),
        ('Computer','Computer'),
        ('Hindi','Hindi'),
        ('English','English'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    subject = models.CharField(max_length=20,choices=category_list)
    name = models.CharField(max_length=30)
    phonenumber = models.CharField(max_length=10)
    classestaught = models.IntegerField()