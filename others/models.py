from django.db import models

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
