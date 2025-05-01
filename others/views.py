from django.shortcuts import render
from .models import *


# Create your views here.
def alumni_stories(request):
    alumni = Alumni.objects.all()
    return render(request, 'alumni_stories.html', {'alumni': alumni})

def alumni_association(request):
    pdfs =Alumni_Association.objects.all()
    return render(request, 'alumni_association.html', {'pdfs': pdfs})
