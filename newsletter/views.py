from django.shortcuts import render
from .forms import SignUpForm,ContactForm
from django.core.mail import send_mail
from django.conf import settings
from .models import SignUp


# Create your views here.
def home(request):

    title="Welcome!!! Please Sign Up"
    if request.user.is_authenticated():

        title="Welcome  %s"%(request.user)
    form=SignUpForm(request.POST or None)
    context={
        'title':title,
        'abc':123,
        'form':form
    }
    if form.is_valid():
        instance=form.save(commit=False)
        if not instance.fullname:
            instance.fullname="Random"
        instance.save()
        context={
            'title':"Thank You",
        }

    if request.user.is_authenticated() and request.user.is_staff:

        details={}
        queryset=SignUp.objects.all().order_by('-timestamp')

        context={

            'queryset':queryset
        }

    return render(request,"home.html",context)


def contact(request):

    form=ContactForm(request.POST or None)
    title='Contact Us'

    if form.is_valid():

        # for key,value in form.cleaned_data.iteritems():
        #     print key,value
        email=form.cleaned_data.get("email")
        message=form.cleaned_data.get("message")
        fullname=form.cleaned_data.get("fullname")
        subject="Hello"
        contact_message="We will contact you shortly"
        from_email=settings.EMAIL_HOST_USER
        to_email=[from_email,"amar.prakash196@gmail.com"]

        send_mail(subject,contact_message,from_email,to_email,fail_silently=False)
    context={ 'form':form,
              'title':title,

        }
    return render(request,"form.html",context)
