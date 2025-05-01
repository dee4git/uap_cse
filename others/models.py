from django.db import models
from media import pdfs

# Create your models here.
class Alumni(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    graduation_year = models.IntegerField()
    department = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    bio = models.TextField()
    photo = models.ImageField(upload_to='alumni_photos/')
    def __str__(self):
        return self.name

class Alumni_Association(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='pdfs/', default='pdfs/Alumni_page.pdf')

    def __str__(self):
        return self.title