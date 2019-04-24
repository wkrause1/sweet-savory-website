from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)