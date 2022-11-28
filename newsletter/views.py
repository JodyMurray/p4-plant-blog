from django.shortcuts import render
from django.views.generic import FormView
from newsletter.forms import JoinForm


class NewsLetterForm(FormView):
    template_name = 'index.html'
    form_class = JoinForm
    success_url = '/'

  
