from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from .models import *
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage



def index(request):
    return render(request, 'donuts/index.html')

def donuts(request):
    donuts = Donuts.objects.all()
    context = {
        'donuts' : donuts
    }
    return render(request, 'donuts/donuts.html', context)

def email(request):
    form_class = ContactForm(request.POST or None)

    if request.method == 'POST':
        message = request.POST['message']
        subject = request.POST['subject']
        email = EmailMessage(subject, message, to=['blakeygriffy@gmail.com'])
        email.send()
        #return render(request, 'donuts/contact-us.html')

    form = form_class
    context = {
        'form': form
    }
    return render(request, 'donuts/contact-us.html', context)
