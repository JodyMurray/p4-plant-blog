from django.shortcuts import render
from django.views.generic import FormView
from newsletter.forms import JoinForm
from .models import NewsLetter


def newsletter_signup(request):
    form = JoinForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetter.objects.filter(email=instance.email).exists():
            print('Sorry this email already exists')
        else:
            instance.save()

    context = {
        'form': form,
    }
    template = "newsletter/register.html"
    return render(request, template, context)


def newsletter_unsubscribe(request):
    form = JoinForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetter.objects.filter(email=instance.email).exists():
            NewsLetter.objects.filter(email=instance.email).delete()
        else:
            print("Sorry, but we did not find your email address")

    context = {
        'form': form,
    }
    template = "newsletter/unsubscribe.html"
    return render(request, template, context)
  
