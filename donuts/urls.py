from django.urls import path

from . import views

app_name = 'donuts'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('donuts/', views.donuts, name = 'donuts'),
    ]