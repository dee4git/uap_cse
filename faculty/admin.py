from django.contrib import admin
from .models import Faculty
from .models import AllowedEmail

admin.site.register(Faculty)
admin.site.register(AllowedEmail)
