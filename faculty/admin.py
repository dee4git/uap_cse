from django.contrib import admin
from django.db import models
from .models import Faculty, AllowedEmail

admin.site.register(AllowedEmail)

class FacultyAdmin(admin.ModelAdmin):
    ordering = ('sl',)

    def get_queryset(self, request):
        return Faculty.custom.all()

    def delete_queryset(self, request, queryset):
        for obj in queryset.order_by('sl'):
            Faculty.custom.delete_member(obj.sl)

    def save_model(self, request, obj, form, change):
        if not change:
            Faculty.custom.insert_member(obj.name, obj.sl)
        else:
            old_obj = Faculty.objects.get(pk=obj.pk)
            old_sl = old_obj.sl
            new_sl = obj.sl

            if new_sl != old_sl:
                if new_sl < old_sl:
                    Faculty.objects.filter(sl__gte=new_sl, sl__lt=old_sl).exclude(
                        pk=obj.pk).update(sl=models.F('sl') + 1)
                else:
                    Faculty.objects.filter(sl__gt=old_sl, sl__lte=new_sl).exclude(
                        pk=obj.pk).update(sl=models.F('sl') - 1)

            super().save_model(request, obj, form, change)

    def delete_model(self, request, obj):
        Faculty.custom.delete_member(obj.sl)

admin.site.register(Faculty, FacultyAdmin)