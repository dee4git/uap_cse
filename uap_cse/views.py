from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def faculty(request):
    return render(request, 'faculty.html')
def alumni(request):
    return render(request, 'Alumni.html')
def alumni_stories(request):
    return render(request, 'Alumni_Stories.html')
def alumni_association(request):
    return render(request, 'Alumni_Association.html')