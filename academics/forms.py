from django import forms
from .models import NoticeBoard

class NoticeBoardForm(forms.ModelForm):
    class Meta:
        model = NoticeBoard
        fields = ['title', 'image', 'description', 'is_active']
