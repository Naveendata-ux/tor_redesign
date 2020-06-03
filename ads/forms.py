from django import forms
from django.core.exceptions import ValidationError

from core.models import *
from django.utils.translation import pgettext_lazy
from django.forms.widgets import CheckboxSelectMultiple, TextInput, Select


class AdTypeSelectorForm(forms.ModelForm):
    """Form that allows selecting product type."""

    ad_type = forms.ModelChoiceField(
        queryset=AdType.objects.all(),
        label=pgettext_lazy("Ad type form label", "Ad type"),
        widget=forms.RadioSelect,
        empty_label=None,
    )

class AdTypeForm(forms.ModelForm):
   
   
    ad_attributes = forms.ModelMultipleChoiceField(
        queryset=Attribute.objects.none(),
        required=False,
        label=pgettext_lazy(
            "Ad type attributes", "Attributes common to all variants."
        ),
    )
    

    class Meta:
        model = AdType
        exclude = []
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #manager = get_extensions_manager()
        ad_attrs_qs = Attribute.objects.all()
       

        if self.instance.pk:
            ad_attrs_initial = (
                self.instance.ad_attributes.all()
            )
            
        else:
            ad_attrs_initial = []
            variant_attrs_initial = []

        self.fields["ad_attributes"].queryset = ad_attrs_qs
        self.fields["ad_attributes"].initial = ad_attrs_initial
        

    def clean(self):
        data = super().clean()
        has_attributes = self.cleaned_data["has_attributes"]
        ad_attr = set(self.cleaned_data.get("ad_attributes", []))
        
        if not has_attributes:
            msg = pgettext_lazy(
                "Ad type form error", "Ad variants are disabled."
            )
            self.add_error("variant_attributes", msg)
        if ad_attr:
            msg = pgettext_lazy(
                "Ad type form error",
                "A single attribute can't belong to both a ad " 
            )
            
        if not self.instance.pk:
            return data

        

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        new_ad_attrs = self.cleaned_data.get("ad_attributes", [])
        
        #instance.ad_attributes.set(new_ad_attrs)
        
        return instance


class AttributesMixin:
    """Form mixin that dynamically adds attribute fields."""

    available_attributes = Attribute.objects.none()

    def prepare_fields_for_attributes(self):
        initial_attrs = self.instance.attributes

        for attribute in self.available_attributes:

            attribute_rel = initial_attrs.filter(
                assignment__attribute_id=attribute.pk
            ).first()
            initial = None if attribute_rel is None else attribute_rel.values.first()

            field_defaults = {
                "label": attribute.name,
                "required": False,
                "initial": initial,
            }

            if attribute.has_values():
                field = ModelChoiceOrCreationField(
                    queryset=attribute.values.all(), **field_defaults
                )
            else:
                field = forms.CharField(**field_defaults)

            self.fields[attribute.get_formfield_name()] = field

    def iter_attribute_fields(self):
        """In use in templates to retrieve the attributes input fields."""
        for attr in self.available_attributes:
            yield self[attr.get_formfield_name()]

    def save_attributes(self):
        assert self.instance.pk is not None, "The instance must be saved first"

        for attr in self.available_attributes:
            value = self.cleaned_data.pop(attr.get_formfield_name())

            # Skip if no value was supplied for that attribute
            if not value:
                continue

            # If the passed attribute value is a string, create the attribute value.
            if not isinstance(value, AttributeValue):
                value = AttributeValue.objects.create(
                    attribute_id=attr.pk, name=value, slug=slugify(value)
                )

            associate_attribute_values_to_instance(self.instance, attr, value)




class AttributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = ("name",)
        
        
class AttributeValueForm(forms.ModelForm):
    class Meta:
        model = AttributeValue
        fields = ["attribute", "name","value",]
        

    def save(self, commit=True):
        return super().save(commit=commit)
   

class AdCreateForm(forms.ModelForm):
    class Meta:
        model = Ad
        #exclude = ('tyre','wheels')
        fields = ( 'title', 'description', 'price', 'location')
        

class AdUpdateForm(forms.ModelForm):
    class Meta:
        model = Ad
        exclude = ("user",)

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

class TyresForm(forms.ModelForm):
    
    class Meta:
        model =Tyres
        fields = ('Add_Title', 'Tire_Condition', 'On_Rims','Year','Make','Model','Width','Ratio','Diameter','Tyres_Available','Rent_Type','Seasonality')
        
class WheelsForm(forms.ModelForm):
    class Meta:
        model =Wheels
        fields = ('Add_Title', 'Wheels_Brand','Width','Ratio','Diameter', 'Offer_Price', 'Seasonality')
        
