from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=11)
    bio = models.TextField(max_length=200)
    about = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.user.first_name + " " + self.user.last_name}'

class AllowedEmail(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email