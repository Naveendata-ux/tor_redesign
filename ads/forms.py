from django import forms
from django.core.exceptions import ValidationError

from core.models import *
from django.utils.translation import pgettext_lazy
from django.forms.widgets import CheckboxSelectMultiple, TextInput, Select



class AdCreateForm(forms.ModelForm):
    
    Ad_title = forms.CharField(error_messages={'invalid': 'Give a suitble name for your Ad!'})
    #category = forms.CharField(error_messages={'invalid': 'Please select a valid Category!'})
    description = forms.CharField(error_messages={'invalid': 'Please fill description field!'})
    offer_price = forms.IntegerField(error_messages={'invalid': 'Please enter offer price!'})
    location = forms.CharField(error_messages={'invalid': 'Please enter location!'})
    Tire_Condition = forms.CharField(error_messages={'invalid': 'Please select a valid Choice for Tire_Condition!'})
    On_Rims = forms.CharField(error_messages={'invalid': 'Please select a valid Choice for Rims!'})
    Make = forms.CharField(error_messages={'invalid': 'Please select a valid Choice for Make!'})
    Width = forms.IntegerField(error_messages={'invalid': 'Please select a valid Choice for Width!'})
    Year = forms.IntegerField(error_messages={'invalid': 'Please select a valid Year!'})
    
    Aspect_Ratio = forms.IntegerField(error_messages={'invalid': 'Please select a valid Choice for Ratio!'})
    tires_available = forms.IntegerField(error_messages={'invalid': 'Please enter value for Tyres_Available!'})
    #Tenure_offered = forms.IntegerField(error_messages={'invalid': 'Please enter value for Tenure_offered!'})
    Ad_Type = forms.CharField(error_messages={'invalid': 'Please select valid choice for Ad_Type!'})
    Seasonality= forms.CharField(error_messages={'invalid': 'Please Select valid choice for Seasonality!'})
   
    class Meta:
        model = Ad
        #exclude = ('tyre','wheels')
        fields = ( 'Ad_title', 'description', 'category','offer_price','Tire_Condition', 'On_Rims', 'Year','Make','Model','Width','Aspect_Ratio',
        'tires_available','Tenure_offered','Ad_Type', 'Seasonality')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(AdCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        self._validate_unique = True
        self.validate_ad_images()
        return self.cleaned_data

    def validate_ad_images(self):
        images = self.request.FILES.getlist('image')
        if images:
            for image in images:
                if image.size > 1 * 1024 * 1024:
                    raise ValidationError("Image file too large ( > 1mb )")
        else:
            raise ValidationError("Couldn't read uploaded images")

    

class AdUpdateForm(forms.ModelForm):
    Ad_title = forms.CharField(error_messages={'invalid': 'Give a suitble name for your Ad!'})
    #category = forms.CharField(error_messages={'invalid': 'Please select a valid Category!'})
    Width = forms.CharField(error_messages={'invalid': 'Please select a valid Choice!'})
   # Year = forms.ChoiceField(error_messages={'invalid': 'Please select a valid Year!'})
    
    Aspect_Ratio = forms.CharField(error_messages={'invalid': 'Please select a valid Choice!'})
    
    
    class Meta:
        model = Ad
        fields = ( 'Ad_title', 'description', 'category','offer_price', 'location','Tire_Condition', 'On_Rims','Year','Make','Model','Width','Aspect_Ratio','tires_available','Tenure_offered','Ad_Type', 'Seasonality')
        
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(AdUpdateForm, self).__init__(*args, **kwargs)

    def clean(self):
        self._validate_unique = True
        if len(self.request.FILES.getlist('image')) > 0:
            self.validate_ad_images()
        return self.cleaned_data

    def validate_ad_images(self):
        images = self.request.FILES.getlist('image')
        if images:
            for image in images:
                if image.size > 1 * 1024 * 1024:
                    raise ValidationError("Image file too large ( > 1mb )")
        else:
            raise ValidationError("Couldn't read uploaded images")

class AdImageForm(forms.ModelForm):
    class Meta:
        model = AdImage
        fields = ("image",)

   
