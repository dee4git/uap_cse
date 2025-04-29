

# Register your models here.
from django.contrib import admin
from .models import PDFFile
from .models import AdmissionResult


admin.site.register(PDFFile)

admin.site.register(AdmissionResult)

from .models import NoticeBoard

@admin.register(NoticeBoard)
class NoticeBoardAdmin(admin.ModelAdmin):
    list_display = ('title', 'upload_date', 'is_active')
    search_fields = ('title', 'description')
    list_filter = ('is_active',)


from .models import Routine

@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = ('title', 'routine_type', 'year', 'semester', 'section', 'upload_date')
    list_filter = ('routine_type', 'year', 'semester', 'section')
