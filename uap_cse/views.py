from django.shortcuts import render


def home(request):
    return render(request, 'home.html')
def faculty(request):
    return render(request, 'faculty.html')

def undergraduate(request):
    return render(request, 'hard_html/undergraduate.html')

def graduate(request):
    return render(request, 'hard_html/graduate.html')

def tuition(request):
    return render(request, 'hard_html/tuition.html')

def why_cse(request):
    return render(request, 'hard_html/why_cse.html')

def host(request):
    return render(request, 'hard_html/icpc_host.html')

def clubs(request):
    return render(request, 'hard_html/clubs.html')
def club_detail(request):
    return render(request, 'club_detail.html')
def gallery(request):
    return render(request, 'hard_html/gallery.html')