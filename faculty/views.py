from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, UpdateForm
from .models import Faculty

from django.shortcuts import render, get_object_or_404
from .scholar_api import get_or_cache_best_papers


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            profile = Faculty(user=user)
            profile.save()

            login(request, user)
            return redirect('update')
        else:
            return render(request, 'signup.html', {
                'form': form,
            })
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {
        'form': form,
    })


@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # If authentication is successful
            login(request, user)
            return redirect('update')
        else:
            # If authentication fails
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html')

@login_required
def update_view(request):
    try:
        faculty = Faculty.objects.get(user=request.user)
        return render(request, 'update.html', {
            'facultys': [faculty]
        })

    except Faculty.DoesNotExist:
        messages.error(request, "No faculty profile found for your account")
        return redirect('login')

@login_required
def update_faculty(request, pk):
    p = Faculty.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('update')
    else:
        form = UpdateForm(instance=p)
    return render(request, 'forms.html', {'form': form})

def faculty_research(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    papers = get_or_cache_best_papers(faculty.google_scholar_url)

    context = {
        'faculty': faculty,
        'papers': papers
    }

    return render(request, 'faculty/faculty_research.html', context)


