from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail
from newsletter.forms import JoinForm
from .models import NewsLetter
from django.template.loader import render_to_string


# https://www.youtube.com/watch?v=yZPgBThZT04&list=PLGzru6ACxEAKtb29AeyHbVGUh2-0r891H&index=27
# The above link was a useful guide.
def newsletter_signup(request):
    """
    Function that allows users to
    sign up to the newsletter
    """
    if request.method == 'POST':
        form = JoinForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            if NewsLetter.objects.filter(email=instance.email).exists():
                messages.warning(
                    request, "Your email already exists in our database",
                    "alert alert-warning alert-dismissible")

            else:
                instance.save()
                messages.success(
                    request,
                    "Your email has been submitted to the database",
                    "alert alert-success alert-dismissible"
                    )
            email = form.cleaned_data['email']
            print(form.cleaned_data['email'])
            print('Email valid')
            to_email = [instance.email]

            html = render_to_string(
                'newsletter/email.html',
                {'email': email}
            )

        send_mail(
            'subject',
            'message',
            settings.EMAIL_HOST_USER,
            [email],
            html_message=html
        )

    else:
        form = JoinForm(request.POST)

    return render(
        request,
        'newsletter/register.html',
        {'form': form}
    )


def newsletter_unsubscribe(request):
    """
    Function that allows user to unsubscribe to newsletter
    """
    form = JoinForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetter.objects.filter(email=instance.email).exists():
            NewsLetter.objects.filter(email=instance.email).delete()
            messages.success(
                request,
                "Your email has been removed",
                "alert alert-success alert-dismissible"
            )
            subject = "You have unsubscribed to our Newsletter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            signup_message = """ Sorry to see you go,
            let us know if there is an issue with our service """
            send_mail(
                subject=subject,
                from_email=from_email,
                recipient_list=to_email,
                message=signup_message,
                fail_silently=False
            )
        else:
            messages.warning(
                request,
                "Your email is not in the database",
                "alert alert-warning alert-dismissible"
            )

    context = {
        'form': form,
    }
    template = "newsletter/unsubscribe.html"
    return render(
        request,
        template,
        context
    )
