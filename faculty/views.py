from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission

from django.contrib.contenttypes.models import ContentType


from .forms import SignUpForm
from .forms import UpdateForm
from .models import Faculty


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
def update_faculty(request, pk):
    p = Faculty.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return HttpResponse('Updated Successfully')
    else:
        form = UpdateForm(instance=p)
    return render(request, 'forms.html', {'form': form})

@login_required
def update_view(request):
    facultys = Faculty.objects.all()
    return render(request, 'update.html',{
        'facultys' : facultys
    })




