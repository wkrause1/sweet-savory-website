from django.urls import path

from . import views

app_name = 'donuts'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('sweet/', views.sweet, name ='donuts'),
    path('contact-us/', views.contact, name = 'contact'),
    path('savory/', views.savory, name = 'savory'),
    path('drinks/', views.drinks, name = 'drinks'),
    ]