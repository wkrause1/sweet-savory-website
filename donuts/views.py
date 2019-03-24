from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse
from .models import Product

def index(request):
    return render(request, 'donuts/index.html')

def donuts(request):
    donuts = Product.objects.all()
    context = {
        'donuts' : donuts
    }
    return render(request, 'donuts/donuts.html', context)