from django.contrib import messages
from django.shortcuts import render
from django.views.generic import FormView
from newsletter.forms import JoinForm
from .models import NewsLetter



def newsletter_signup(request):
    form = JoinForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetter.objects.filter(email=instance.email).exists():
            messages.warning(
                request, "Your email already exists in our database", 
                "alert alert-warning alert-dismissible")
        else:
            instance.save()
            messages.success(request, "Your email has been submitted to the database",
            "alert alert-success alert-dismissible")

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
            messages.success(request, "Your email has been removed",
            "alert alert-success alert-dismissible")
        else:
            messages.warning(request, "Your email is not in the database",
            "alert alert-warning alert-dismissible")

    context = {
        'form': form,
    }
    template = "newsletter/unsubscribe.html"
    return render(request, template, context)
  
