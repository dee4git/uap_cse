from django import forms
from django.contrib.auth.models import User
from .models import AllowedEmail, Faculty


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
            'google_scholar_url',

        ]
        help_texts = {
            'joining_date': 'Date format: YYYY-MM-DD',
        }


# faculty sl change form
class FacultySerialNumberForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['sl']  # Only the 'sl' field will be used for updating serial numbers

    def clean_sl(self):
        new_sl = self.cleaned_data['sl']

        # Check if the new serial number already exists
        if Faculty.objects.filter(sl=new_sl).exists():
            raise forms.ValidationError("This serial number already exists. Please choose a different number.")

        return new_sl

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Shift all faculties with a greater serial number by 1
        if instance.sl:
            # Fetch all faculties with a serial number greater than the new sl
            faculties_to_shift = Faculty.objects.filter(sl__gte=instance.sl).exclude(id=instance.id)
            for faculty in faculties_to_shift:
                faculty.sl += 1
                faculty.save()

        if commit:
            instance.save()
        return instance
