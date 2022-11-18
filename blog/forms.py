from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Comment, Profile
from django import forms


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'user',
            'first_name',
            'last_name',
            'profile_pic',
            'bio'
        )
        exclude = ['user']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
