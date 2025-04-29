from django.shortcuts import render

# Create your views here.
from academics.models import PDFFile

def show_pdf(request):
    pdfs = PDFFile.objects.all()
    return render(request, 'curriculum.html', {'pdfs': pdfs})

from academics.models import AdmissionResult

def admission_result_view(request):
    context = {
        'written_results': AdmissionResult.objects.filter(result_type='written', is_active=True),
        'final_results': AdmissionResult.objects.filter(result_type='final', is_active=True),
        'waiting_results': AdmissionResult.objects.filter(result_type='waiting', is_active=True),
    }
    return render(request, 'admission_result.html', context)
from django.shortcuts import render
from .models import NoticeBoard

def notice_board_view(request):
    notices = NoticeBoard.objects.filter(is_active=True)  # Fetch only active notices
    return render(request, 'notice_board.html', {'notices': notices})


from django.shortcuts import render, redirect
from .models import NoticeBoard
from .forms import NoticeBoardForm


def add_notice_view(request):
    if request.method == 'POST':
        form = NoticeBoardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notice_board')  # Redirect to the notice board page
    else:
        form = NoticeBoardForm()

    return render(request, 'add_notice.html', {'form': form})

from django.shortcuts import render
from .models import Routine

def routine_view(request):
    routine_type = request.GET.get('type', 'class')
    year = request.GET.get('year')
    semester = request.GET.get('semester')
    section = request.GET.get('section') if routine_type == 'class' else None

    routines = Routine.objects.filter(routine_type=routine_type)

    if year:
        routines = routines.filter(year=year)
    if semester:
        routines = routines.filter(semester=semester)
    if section:
        routines = routines.filter(section=section)

    context = {
        'routines': routines,
        'selected_type': routine_type,
        'selected_year': year,
        'selected_semester': semester,
        'selected_section': section,
    }
    return render(request, 'routine_view.html', context)
from django.shortcuts import render

def waiver(request):
    # You can pass additional context here if needed
    context = {
        # Add context data if you want to pass dynamic content to the template
    }
    return render(request, 'hard_html/waiver.html', context)
