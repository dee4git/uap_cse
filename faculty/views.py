from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission

from django.contrib.contenttypes.models import ContentType


from .forms import SignUpForm
from .models import Profile


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            full_name = form.cleaned_data.get('full_name').strip()
            name_parts = full_name.split()
            user.first_name = name_parts[0]
            user.last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ''

            user.set_password(form.cleaned_data['password'])
            user.is_staff = True
            user.save()

            profile = Profile(user=user)
            profile.save()

            content_type = ContentType.objects.get_for_model(Profile)

            view_permission = Permission.objects.get(codename='view_profile', content_type=content_type)
            change_permission = Permission.objects.get(codename='change_profile', content_type=content_type)

            user.user_permissions.set([view_permission, change_permission])

            login(request, user)
            return redirect('home')
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
            # If authentication is successful, log the user in
            login(request, user)
            return redirect('home')
        else:
            # If authentication fails, show an error message
            messages.error(request, "Invalid username or password")
            return redirect('login')
    return render(request, 'login.html')

@login_required
def home(request):
    return render(request, 'home.html')




