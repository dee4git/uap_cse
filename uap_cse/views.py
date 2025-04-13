from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def faculty(request):
    return render(request, 'faculty.html')

def undergraduate(request):
    return render(request, 'undergraduate.html')

def graduate(request):
    return render(request, 'graduate.html')
def international(request):
    return render(request, 'international.html')
