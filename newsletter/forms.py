from django import forms
from .models import NewsLetter
from crispy_forms.helper import FormHelper


class JoinForm(forms.ModelForm):
    """ Newsletter form view """

    helper = FormHelper()
    helper.form_show_labels = False

    class Meta:
        model = NewsLetter
        fields = ['email']

        def clean_email(self, *args, **kwargs):
            email = self.cleaned_data.get(
                'email'
            )
            queryset = NewsLetter.objects.filter(
                email__iexact=email
            )
            if queryset.exists():
                raise forms.ValidationError(
                    'This email already exists'
                )
            return email
