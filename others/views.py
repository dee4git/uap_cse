from django.shortcuts import render
from .models import *


# Create your views here.
def alumni_stories(request):
    alumni = Alumni.objects.all()
    return render(request, 'alumni/alumni_stories.html', {'alumni': alumni})
def alumni(request):
    alumni = Alumni.objects.all()
    return render(request, 'alumni/alumni.html', {'alumni': alumni})

def alumni_association(request):
    alumni_association =Alumni_Association.objects.all()
    return render(request, 'alumni/alumni_association.html', {'alumni_association': alumni_association})
