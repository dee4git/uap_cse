from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def faculty(request):
    return render(request, 'faculty.html')