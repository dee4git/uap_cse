from django.contrib import admin

# Register your models here.
from .models import Alumni, Alumni_Association

admin.site.register(Alumni)
admin.site.register(Alumni_Association)