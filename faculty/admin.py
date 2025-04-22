from django.contrib import admin
from .models import Profile
from .models import AllowedEmail

admin.site.register(Profile)
admin.site.register(AllowedEmail)
