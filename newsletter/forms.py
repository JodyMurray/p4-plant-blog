from django import forms
from .models import NewsLetter


class JoinForm(forms.ModelForm):
    email = forms.EmailField(
        label='', widget=forms.EmailInput(
            attrs={'placeholder': 'Your email', 'class': 'form-control'}))

    class Meta:
        model = NewsLetter
        fields = ['email']

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        queryset = NewsLetter.objects.filter(email__iexact=email)
        if queryset.exists():
            raise forms.ValidationError("This email already exists")
        return email
        print(email)
