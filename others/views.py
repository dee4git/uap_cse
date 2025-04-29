from django.shortcuts import render
from .models import Alumni
# Create your views here.
def alumni_stories(request):
    alumni = Alumni.objects.all()
    return render(request, 'alumni_stories.html', {'alumni': alumni})
