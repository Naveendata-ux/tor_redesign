from django import forms
from django.forms import ModelForm
from core.models import *

class ContactForm(forms.ModelForm):

    Name= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your first name'}))
    Email= forms.CharField(widget= forms.EmailInput
                           (attrs={'placeholder':'email@gmail.com'}))
    Subject= forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter Subject'}))
    Message= forms.CharField(widget= forms.Textarea 
                           (attrs={'placeholder':'Enter Message <250 words'}))



    class Meta:
        model=Contact
        fields=('Name','Email','Subject','Message')
