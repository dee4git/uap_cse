from django.contrib import admin

# Register your models here.
from .models import Alumni, Alumni_Association

admin.site.register(Alumni)

from django.contrib import admin
from .models import Alumni_Association

@admin.register(Alumni_Association)
class Alumni_AssociationAdmin(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')
    search_fields = ('title',)
    list_filter = ('title',)
