from django import forms
from django.core.exceptions import ValidationError

from core.models import *
from django.utils.translation import pgettext_lazy
from django.forms.widgets import CheckboxSelectMultiple, TextInput, Select



class AdCreateForm(forms.ModelForm):
    class Meta:
        model = Ad
        #exclude = ('tyre','wheels')
        fields = ( 'Ad_title', 'description', 'category','offer_price', 'location','Tire_Condition', 'On_Rims','Year','Make','Model','Width','Aspect_Ratio','Tyres_Available','Tenure_offered','Ad_Type','Wheels_Brand', 'Seasonality')
    
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
    class Meta:
        model = Ad
        fields = ( 'Ad_title', 'description', 'category','offer_price', 'location','Tire_Condition', 'On_Rims','Year','Make','Model','Width','Aspect_Ratio','Seasonality','Tenure_offered','Tyres_Available','Ad_Type','Wheels_Brand', )

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

   
