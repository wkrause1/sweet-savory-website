from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from .models import *

def index(request):
    return render(request, 'donuts/index.html')

def sweet(request):
    sweets = Donuts.objects.all()
    context = {
        'donuts' : sweets
    }
    return render(request, 'donuts/donuts.html', context)

def savory(request):
    savories = Sandwiches.objects.all()
    context = {
        'savories' : savories
    }
    return render(request, 'donuts/savory.html', context)

def drinks(request):
    drinks = Drinks.objects.all()
    context = {
        'drinks' : drinks
    }
    return render(request, 'donuts/drinks.html', context)

def contact(request):
    return render(request, 'donuts/contact-us.html')
