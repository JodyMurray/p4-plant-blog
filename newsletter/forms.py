from django import forms
from .models import NewsLetter

class JoinForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']