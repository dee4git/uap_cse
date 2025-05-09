from django.contrib import admin
from .models import Club, ClubMember

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')
    search_fields = ('name',)

@admin.register(ClubMember)
class ClubMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'club', 'position', 'email')  # Fields to display in the admin list view
    search_fields = ('user__username', 'club__name', 'position')  # Fields to search by
    list_filter = ('club', 'position')  # Filters for the admin panel
    autocomplete_fields = ('user', 'club')  # Enable autocomplete for related fields