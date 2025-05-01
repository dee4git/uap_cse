

# Register your models here.
from django.contrib import admin

from .models import AdmissionResult

# admin.py
from django.contrib import admin
from .models import Mission

@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')  # Display the title and the PDF file field
    search_fields = ('title',)  # Enable search by title in the admin
    list_filter = ('title',)  # Enable filtering by title
# admin.py
from django.contrib import admin
from .models import AcademicCalendar

@admin.register(AcademicCalendar)
class AcademicCalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')
    search_fields = ('title',)
# admin.py
from django.contrib import admin
from .models import ICPCEventSection

@admin.register(ICPCEventSection)
class ICPCEventSectionAdmin(admin.ModelAdmin):
    list_display = ('section_title', 'section_order')
    list_editable = ('section_order',)
    search_fields = ('section_title',)
    ordering = ('section_order',)
# admin.py
from django.contrib import admin
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', 'image')  # Display title, publish date, and image in the list
    search_fields = ('title', 'description')  # Enable search by title and description

admin.site.register(Notice, NoticeAdmin)



from .models import Routine

@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('year', 'semester', 'section')
    list_filter = ('year', 'semester', 'section')

from django.contrib import admin
from .models import ExamRoutine

class ExamRoutineAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Display title and image in the list view
    list_filter = ('title',)  # You can filter by title, or remove if unnecessary

admin.site.register(ExamRoutine, ExamRoutineAdmin)
from django.contrib import admin
from .models import AdmissionResult

# admin.py
from django.contrib import admin
from .models import AdmissionResult

class AdmissionResultAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'upload_date', 'image')
    search_fields = ('title', 'category')

admin.site.register(AdmissionResult, AdmissionResultAdmin)
# admin.py
from django.contrib import admin
from .models import Curriculum

# Register the Curriculum model with the admin site
@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    # Define the fields you want to display in the admin panel
    list_display = ('title', 'pdf_file')  # Display title and PDF file field in the list view
    search_fields = ('title',)  # Allow searching by the title
    list_filter = ('title',)  # Add a filter option for the title field

    # You can customize other aspects of the admin panel here as needed
    # For example, you can include other fields in the form layout, add custom actions, etc.

