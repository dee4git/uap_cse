from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User
from faculty.models import Faculty


from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os

class Club(models.Model):
    convener = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='club_logos/', default='defaults/clubcover.png')
    moto = models.CharField(max_length=255)
    cover_picture = models.ImageField(upload_to='club_covers/', default='defaults/clubcover.png')
    description = models.TextField()
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Auto-process logo (1:1)
        if self.logo:
            logo_path = self.logo.path
            img = Image.open(logo_path)

            width, height = img.size
            min_dim = min(width, height)
            left = (width - min_dim) / 2
            top = (height - min_dim) / 2
            right = (width + min_dim) / 2
            bottom = (height + min_dim) / 2
            img_cropped = img.crop((left, top, right, bottom))

            img_resized = img_cropped.resize((300, 300))  # You can adjust final size
            img_resized.save(logo_path, optimize=True, quality=85)

        # Auto-process cover picture (21:9)
        if self.cover_picture:
            cover_path = self.cover_picture.path
            img = Image.open(cover_path)

            width, height = img.size
            target_ratio = 21 / 9

            # Calculate new cropping box
            current_ratio = width / height

            if current_ratio > target_ratio:
                # Too wide, crop sides
                new_width = int(height * target_ratio)
                left = (width - new_width) / 2
                top = 0
                right = (width + new_width) / 2
                bottom = height
            else:
                # Too tall, crop top/bottom
                new_height = int(width / target_ratio)
                left = 0
                top = (height - new_height) / 2
                right = width
                bottom = (height + new_height) / 2

            img_cropped = img.crop((left, top, right, bottom))
            img_resized = img_cropped.resize((1680, 720))  # 21:9 resolution, optional
            img_resized.save(cover_path, optimize=True, quality=85)

    def __str__(self):
        return self.name


class ClubMember(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # club member = user
    position = models.CharField(max_length=100)
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='club_members/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.position} ({self.club.name})"


class ClubPost(models.Model):
    POST_TYPES = [
        ('announcement', 'Announcement'),
        ('event', 'Event Details'),
        ('other', 'Other'),
    ]

    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(ClubMember, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    post_type = models.CharField(max_length=20, choices=POST_TYPES)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    cover_photo = models.ImageField(upload_to='club_posts/', null=True, blank=True)
    pic1 = models.ImageField(upload_to='club_posts/', null=True, blank=True)
    pic2 = models.ImageField(upload_to='club_posts/', null=True, blank=True)
    pic3 = models.ImageField(upload_to='club_posts/', null=True, blank=True)
    pic4 = models.ImageField(upload_to='club_posts/', null=True, blank=True)
    pic5 = models.ImageField(upload_to='club_posts/', null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.club.name})"
