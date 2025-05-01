from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render
from .models import Curriculum

def curriculum_view(request):
    curriculums = Curriculum.objects.all()
    return render(request, 'curriculum.html', {
        'curriculums': curriculums,
    })
# views.py
from django.shortcuts import render
from .models import Mission

def mission_view(request):
    missions = Mission.objects.all()  # Fetch all the mission PDFs from the database
    return render(request, 'mission.html', {
        'missions': missions,
    })
# views.py
from django.shortcuts import render
from .models import AcademicCalendar

def academic_calendar_view(request):
    calendars = AcademicCalendar.objects.all()
    return render(request, 'academic_calendar.html', {
        'calendars': calendars
    })
# views.py
from django.shortcuts import render
from .models import ICPCEventSection

def icpc_event_view(request):
    sections = ICPCEventSection.objects.all()
    return render(request, 'icpc_event.html', {'sections': sections})

# views.py
from django.shortcuts import render
from .models import AdmissionResult


def admission_result_view(request):
    written_results = AdmissionResult.objects.filter(category='written')
    final_results = AdmissionResult.objects.filter(category='final')
    waiting_results = AdmissionResult.objects.filter(category='waiting')

    return render(request, 'admission_result.html', {
        'written_results': written_results,
        'final_results': final_results,
        'waiting_results': waiting_results,
    })


from django.shortcuts import render
# views.py
from django.shortcuts import render, get_object_or_404
from .models import Notice

def notice_board_view(request):
    notices = Notice.objects.all().order_by('-publish_date')  # Display notices sorted by publish date
    return render(request, 'notice_board.html', {'notices': notices})

def notice_detail_view(request, notice_id):
    notice = get_object_or_404(Notice, id=notice_id)
    return render(request, 'notice_detail.html', {'notice': notice})





from django.shortcuts import render
from .models import Routine

# views.py
from django.shortcuts import render
from .models import Routine

def routine_view(request):
    selected_routine = request.GET.get('selected_routine')
    selected_section = request.GET.get('selected_section')

    print(f"Selected Routine: {selected_routine}")
    print(f"Selected Section: {selected_section}")

    # Filter the routines based on selected criteria
    routines = Routine.objects.all()

    if selected_routine:
        routines = routines.filter(year=selected_routine.split('-')[0], semester=selected_routine.split('-')[1])
    if selected_section:
        routines = routines.filter(section=selected_section)

    print(f"Filtered routines count: {routines.count()}")  # To check how many records match

    return render(request, 'routine_view.html', {
        'routines': routines,
        'selected_routine': selected_routine,
        'selected_section': selected_section
    })

# views.py
from django.shortcuts import render
from .models import ExamRoutine

def exam_routine_view(request):
    # Assuming you just want to show the first available exam routine
    exam_routine = ExamRoutine.objects.first()  # This will fetch the first exam routine from the DB
    return render(request, 'exam_routine.html', {'exam_routine': exam_routine})


def waiver(request):
    # You can pass additional context here if needed
    context = {
        # Add context data if you want to pass dynamic content to the template
    }
    return render(request, 'hard_html/waiver.html', context)
