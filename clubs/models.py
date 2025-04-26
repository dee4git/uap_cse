from django.db import models

# Create your models here.


class Club(models.Model):
    name = models.CharField(max_length=100)
    convener = models.CharField(max_length=100)
    co_convener = models.CharField(max_length=100, blank=True, null=True)
    president = models.CharField(max_length=100)
    vice_president = models.CharField(max_length=100)
    general_secretary = models.CharField(max_length=100)
    treasurer = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    images = models.ImageField(upload_to='club_images/')

    def __str__(self):
        return str(self.name)
