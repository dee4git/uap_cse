from django.db import models

# Create your models here.


class PDFFile(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title