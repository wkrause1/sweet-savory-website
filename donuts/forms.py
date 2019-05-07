from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'name'}))
    message = forms.CharField(required=True, widget=forms.TextInput(attrs={'class' : 'message'}))