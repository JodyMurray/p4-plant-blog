from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Comment, Profile, Post
from django import forms


class EditProfileForm(forms.ModelForm):
    """ Function for edit profile """
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
    """ Function for comment form """
    class Meta:
        model = Comment
        fields = [
            'body',
        ]
