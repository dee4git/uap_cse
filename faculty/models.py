from django.contrib.auth.models import User
from django.db import models

from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os


class Faculty(models.Model):
    DESIGNATION_CHOICES = [
        ('PROF', 'Professor'),
        ('ASSO_PROF', 'Associate Professor'),
        ('ASSI_PROF', 'Assistant Professor'),
        ('LECT', 'Lecturer'),
        ('TA', 'Teaching Assistant'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="Name")
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES, null=True)
    phone = models.CharField(max_length=11)
    bio = models.TextField(max_length=200)
    about = models.TextField(max_length=1000)
    profile_pic = models.ImageField(upload_to='faculty_photos/', null=True, blank=True)
    joining_date = models.DateField(null=True)
    google_scholar_url = models.URLField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.profile_pic:
            pic_path = self.profile_pic.path
            img = Image.open(pic_path)

            # Auto-crop to 1:1 (centered square)
            width, height = img.size
            min_dim = min(width, height)
            left = (width - min_dim) / 2
            top = (height - min_dim) / 2
            right = (width + min_dim) / 2
            bottom = (height + min_dim) / 2
            img_cropped = img.crop((left, top, right, bottom))

            # Resize to 300x300
            img_resized = img_cropped.resize((300, 300))

            # Save the processed image (overwrite)
            img_resized.save(pic_path, optimize=True, quality=85)

            # Ensure file size <= 300KB
            if os.path.getsize(pic_path) > 307200:  # 300KB = 300*1024 = 307200 bytes
                img_resized.save(pic_path, optimize=True, quality=70)

    def __str__(self):
        return f'{self.name + " | " + self.designation}'


USER_ROLE_CHOICES = [
    ('3', 'Super Admin'),  # highest access
    ('2', 'Course Access'),  # medium access
    ('1', 'General User'),  # lowest access
]


class AllowedEmail(models.Model):
    role = models.CharField(choices=USER_ROLE_CHOICES, max_length=50, default=1)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
