from ckeditor.fields import RichTextField

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import os
from PIL import Image


class ScholarCache(models.Model):
    scholar_url = models.URLField(unique=True)
    papers = models.JSONField()  # stores list of dicts
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.scholar_url

class FacultyManager(models.Manager):

    def insert_member(self, name, sl):
        self.filter(sl__gte=sl).update(sl=models.F('sl') + 1)
        return self.create(name=name, sl=sl)

    def delete_member(self, sl):
        self.filter(sl=sl).delete()
        self.filter(sl__gt=sl).update(sl=models.F('sl') - 1)

class Faculty(models.Model):
    DESIGNATION_CHOICES = [
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Lecturer', 'Lecturer'),
        ('Teaching Assistant', 'Teaching Assistant'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default="Name")
    shortname = models.CharField(max_length=5, default='N/A')
    designation = models.CharField(max_length=20, choices=DESIGNATION_CHOICES, null=True)
    phone = models.CharField(max_length=11)
    bio = models.TextField(max_length=200)
    about = RichTextField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='faculty_photos/', default='defaults/faculty.png', null=True, blank=True)
    joining_date = models.DateField(null=True)

    # Links
    google_scholar_url = models.URLField(max_length=255, blank=True, null=True)
    researchgate_url = models.URLField(max_length=255, blank=True, null=True)
    orcid_url = models.URLField(max_length=255, blank=True, null=True)
    scopus_url = models.URLField(max_length=255, blank=True, null=True)
    linkedin_url = models.URLField(max_length=255, blank=True, null=True)

    citation = models.PositiveIntegerField(default=0, blank=True, null=True)
    sl = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    # Routine upload (PDF/image)
    routine = models.FileField(upload_to='faculty_routines/', null=True, blank=True)

    # Default manager
    objects = models.Manager()
    custom = FacultyManager()

    def save(self, *args, **kwargs):

        if self._state.adding:
            max_sl = Faculty.objects.aggregate(models.Max('sl'))['sl__max']
            self.sl = 1 if max_sl is None else max_sl + 1

        super().save(*args, **kwargs)

        if self.profile_pic:
            pic_path = self.profile_pic.path
            img = Image.open(pic_path)

            width, height = img.size
            min_dim = min(width, height)
            left = (width - min_dim) / 2
            top = (height - min_dim) / 2
            right = (width + min_dim) / 2
            bottom = (height + min_dim) / 2
            img_cropped = img.crop((left, top, right, bottom))
            img_resized = img_cropped.resize((600, 600))
            img_resized.save(pic_path, optimize=True, quality=100)

            if os.path.getsize(pic_path) > 307200:
                img_resized.save(pic_path, optimize=True, quality=70)

    def __str__(self):
        return f'{self.sl}. {self.name} | {self.designation}'


USER_ROLE_CHOICES = [
    ('5', 'Head'),          # highest access
    ('4', 'Super Admin'),   # highest access
    ('3', 'Course Access'), # medium access
    ('2', 'General User'),  # lower access
    ('1', 'Club Member'),   # lowest access
]

class AllowedEmail(models.Model):
    role = models.CharField(choices=USER_ROLE_CHOICES, max_length=50, default=1)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
