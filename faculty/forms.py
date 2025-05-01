from django import forms
from django.contrib.auth.models import User
from .models import AllowedEmail, Faculty
from django.contrib.auth.forms import PasswordResetForm


class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered.")

        if not AllowedEmail.objects.filter(email=email).exists():
            raise forms.ValidationError("Email not authorized.")

        return email


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = [
            'name',
            'joining_date',
            'designation',
            'phone',
            'bio',
            'about',
            'profile_pic',
            'routine',
            'google_scholar_url',
            'researchgate_url',
            'orcid_url',
            'scopus_url',
            'linkedin_url',
        ]
        help_texts = {
            'joining_date': 'Date format: YYYY-MM-DD',
        }


class CustomPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        # Check if the email is in the allowed list
        if not AllowedEmail.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is not authorized for password reset.")

        # Check if the email exists in User model
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError("No user is registered with this email.")

        return email