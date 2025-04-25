from django.contrib.auth.models import User
from django.db import models


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, default="Full Name")
    # last_name = models.CharField(max_length=50, default="Last Name")
    designation = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=11)
    bio = models.TextField(max_length=200)
    about = models.TextField(max_length=1000)
    profile_pic = models.ImageField(upload_to='faculty_photos/', null=True, blank=True)
    joining_date = models.DateField(null=True)
    google_scholar_url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.full_name + " | " + self.designation}'

USER_ROLE_CHOICES = [
    ('3', 'Super Admin'),      # highest access
    ('2', 'Course Access'),    # medium access
    ('1', 'General User'),     # lowest access
]

class AllowedEmail(models.Model):
    role = models.CharField(choices=USER_ROLE_CHOICES, max_length=50, default=1)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
