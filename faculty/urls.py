from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm
from django.urls import path, reverse_lazy
from .import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('update-faculty/<int:pk>', views.update_faculty, name='update-faculty'),
    path('update/', views.update_view, name='update'),
    path('faculty/<int:faculty_id>/research/', views.faculty_research, name='faculty_research'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
        form_class=CustomPasswordResetForm,  
        template_name='password_generic.html',
        extra_context={
            'title': 'Reset Password',
            'heading': 'Reset Your Password',
            'message': 'Enter your email to receive password reset instructions.',
            'button_text': 'Send Reset Email',
        }
    ), name='password_reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_generic.html',
        extra_context={
            'title': 'Email Sent',
            'heading': 'Check Your Inbox',
            'message': 'We’ve emailed instructions to reset your password.',
            'form': None,
            'extra_link_url': '/login/',
            'extra_link_text': 'Return to Login'
        }
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_generic.html',
        success_url=reverse_lazy('password_reset_complete'), 
        extra_context={
            'title': 'Enter New Password',
            'heading': 'Set a New Password',
            'message': '',
            'button_text': 'Change Password',
        }
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_generic.html',
        extra_context={
            'title': 'Password Reset Complete',
            'heading': 'Password Successfully Changed!',
            'message': 'You may now log in with your new password.',
            'form': None,
            'extra_link_url': '/login/',
            'extra_link_text': 'Login Now'
        }
    ), name='password_reset_complete'),
]
