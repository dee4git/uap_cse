from django.db import models

# Create your models here.


class PDFFile(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title


class AdmissionResult(models.Model):
    RESULT_TYPES = [
        ('written', 'Written Test'),
        ('final', 'Final Result'),
        ('waiting', 'Waiting List'),
    ]

    title = models.CharField(max_length=255)
    result_type = models.CharField(max_length=20, choices=RESULT_TYPES)
    pdf_file = models.FileField(upload_to='results/')
    upload_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # for controlling visibility

    class Meta:
        ordering = ['-upload_date']

    def __str__(self):
        return f"{self.get_result_type_display()} - {self.title}"

class NoticeBoard(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='notices/', blank=True, null=True)  # Upload images to 'notices/' directory
    description = models.TextField(blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # To control visibility

    class Meta:
        ordering = ['-upload_date']  # Order by the latest uploaded notice

    def __str__(self):
        return self.title


class Routine(models.Model):
    ROUTINE_TYPES = [
        ('class', 'Class Routine'),
        ('exam', 'Exam Routine'),
    ]

    YEAR_CHOICES = [
        ('1st', '1st Year'),
        ('2nd', '2nd Year'),
        ('3rd', '3rd Year'),
        ('4th', '4th Year'),
    ]

    SEMESTER_CHOICES = [
        ('1st', '1st Semester'),
        ('2nd', '2nd Semester'),
    ]

    SECTION_CHOICES = [
        ('A', 'Section A'),
        ('B', 'Section B'),
        ('C', 'Section C'),
        ('D', 'Section D'),
    ]

    title = models.CharField(max_length=255)
    routine_type = models.CharField(max_length=10, choices=ROUTINE_TYPES)
    year = models.CharField(max_length=3, choices=YEAR_CHOICES)
    semester = models.CharField(max_length=3, choices=SEMESTER_CHOICES)
    section = models.CharField(
        max_length=1,
        choices=SECTION_CHOICES,
        blank=True,
        null=True,
        help_text="Only required for Class Routine"
    )
    image = models.ImageField(upload_to='routines/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_routine_type_display()} - {self.title} ({self.year}, {self.semester}{' - Section ' + self.section if self.section else ''})"
