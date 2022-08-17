from django.db import models

# Create your models here.

class UserRegistration(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    class Meta:
        db_table="user_signup"