from django.db import models

# Create your models here.

# models.py
from django.db import models

class Curriculum(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='curriculums/')

    def __str__(self):
        return self.title
# models.py
from django.db import models

class ICPCEventSection(models.Model):
    section_title = models.CharField(max_length=255)
    paragraph = models.TextField()
    image = models.ImageField(upload_to='icpc_event_images/', null=True, blank=True)
    section_order = models.IntegerField()  # To control the order of sections

    def __str__(self):
        return self.section_title

    class Meta:
        ordering = ['section_order']
# models.py
from django.db import models

class Notice(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='notices/', blank=True, null=True)
    description = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# models.py
from django.db import models

class AdmissionResult(models.Model):
    CATEGORY_CHOICES = [
        ('written', 'Written Test'),
        ('final', 'Final Result'),
        ('waiting', 'Waiting List'),
    ]

    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='admission_results/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='written')
    upload_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='admission_results/images/', null=True, blank=True)  # New Image Field

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"






from django.db import models

class Routine(models.Model):
    YEAR_CHOICES = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year'),
    ]

    SEMESTER_CHOICES = [
        ('1', '1st Semester'),
        ('2', '2nd Semester'),
    ]

    SECTION_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
    ]

    year = models.CharField(max_length=1, choices=YEAR_CHOICES, default='1')
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES , default='1')
    section = models.CharField(max_length=1, choices=SECTION_CHOICES, default='A')
    image = models.ImageField(upload_to='routines/')

    def __str__(self):
        return f"{self.get_year_display()} - {self.get_semester_display()} - Section {self.section}"
from django.db import models

# models.py
from django.db import models

class ExamRoutine(models.Model):
    title = models.CharField(max_length=100)  # Title of the exam routine
    image = models.ImageField(upload_to='exam_routines/')  # Image for the routine

    def __str__(self):
        return self.title

from django.db import models

class Mission(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='missions/')

    def __str__(self):
        return self.title
# models.py
from django.db import models

class AcademicCalendar(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='academic_calendars/')

    def __str__(self):
        return self.title


class Course(models.Model):
    code = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    credit = models.FloatField(default=0.0)
    YEAR = [
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
    ]
    SEMESTER = [
        ('1st','1st'),
        ('2nd','2nd'),
    ]
    year = models.CharField(max_length=15, choices = YEAR, null = True)
    semester = models.CharField(max_length=15, choices = SEMESTER, null = True)

    def __str__(self):
        return f'{self.code}|{self.title}'