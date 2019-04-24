from django.urls import path

from . import views

app_name = 'donuts'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('donuts/', views.donuts, name = 'donuts'),
    #path('contact-us', views.contact, name = 'contact'),
    path('email/', views.email, name='email')
    #path('send', views.send, name='send')
]