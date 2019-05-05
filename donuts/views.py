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

def sweet(request):
    sweets = Sweet.objects.all()
    context = {
        'donuts' : sweets
    }
    return render(request, 'donuts/sweets.html', context)

def savory(request):
    savories = Savory.objects.all()
    context = {
        'savories' : savories
    }
    return render(request, 'donuts/savory.html', context)

def drinks(request):
    drinks = Drink.objects.all()
    context = {
        'drinks' : drinks
    }
    return render(request, 'donuts/drinks.html', context)

def contact(request):
    form_class = ContactForm(request.POST or None)

    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        email = EmailMessage(name, message, to=['blakeygriffy@gmail.com'])
        email.send()
        return HttpResponseRedirect('/')

    form = form_class
    context = {
        'form': form
    }
    return render(request, 'donuts/contact-us.html', context)
