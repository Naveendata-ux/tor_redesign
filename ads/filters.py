from core.models import Ad
from django import forms
import django_filters


CATEGORY_CHOICES = (
    ('1', 'Tires'),
    ('2', 'Wheels'),
    ('3', 'Services'),
    
)

AD_TYPE_CHOICES = (
    ('Rent', 'Rent'),
    ('Rent to Sell', 'Rent to Sell'),
    ('Sell', 'Sell'),
    
)

SEASONALITY_TYPE_CHOICES = (
    ('Summer', 'Summer'),
    ('All Season', 'All Season'),
    ('Winter', 'Winter'),
    
)

SERVICE_TYPE = (
	('Tire Rotation','Tire Rotation'),
	('Tire Repair','Tire Repair'),
	('Wheel Balancing','Wheel Balancing'),
	('Oil Change','Oil Change'),
	('Seasonal Tire Change','Seasonal Tire Change'),
)

Specials_Choices = (

('Limited Time Offer','Limited Time Offer'),
('Seasonal Discounts','Seasonal Discounts'),
('Promotional Discounts','Promotional Discounts'),
('Special Offer','Special Offer')
)


class AdFilter(django_filters.FilterSet):
    category = django_filters.MultipleChoiceFilter(choices=CATEGORY_CHOICES,
                                                   widget=forms.CheckboxSelectMultiple,
                                                   label='<b>CATEGORY</b>')
    Ad_Type = django_filters.MultipleChoiceFilter(choices=AD_TYPE_CHOICES,
                                                   widget=forms.CheckboxSelectMultiple,
                                                   label='<b>Rent Type</b>')
    
    Seasonality = django_filters.MultipleChoiceFilter(choices=SEASONALITY_TYPE_CHOICES,
                                                   widget=forms.CheckboxSelectMultiple,
                                                   label='<b>Seasonality</b>')
    price__gt = django_filters.NumberFilter(field_name='offer_price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='offer_price', lookup_expr='lt') 
    
    Year = django_filters.NumberFilter(label='<b>Year</b>',lookup_expr='exact') 
    Make = django_filters.CharFilter(label='<b>Make</b>',lookup_expr='icontains') 
    Model = django_filters.CharFilter(label='<b>Model</b>',lookup_expr='icontains') 
    location = django_filters.CharFilter(label='<b>Location</b>',lookup_expr='icontains')
    
    
    class Meta:
        model = Ad
        fields = ['category', 'Ad_Type','Seasonality', 'Year','Make','Model','location']
        
class AdFilterServices(django_filters.FilterSet):
	location = django_filters.CharFilter(label='<b>Location</b>',lookup_expr='icontains')
	service_type = django_filters.MultipleChoiceFilter(choices=SERVICE_TYPE,
                                                   widget=forms.CheckboxSelectMultiple,
                                                   label='<b>Service Type</b>') 
	specials = django_filters.MultipleChoiceFilter(choices=Specials_Choices,widget=forms.CheckboxSelectMultiple,label='<b>Special Offers</b>') 
	
	class Meta:
		model = Ad
		fields = ['location','service_type','specials']
        

WHEEL_TYPE_CHOICES = (
    ('Alloy', 'Alloy'),
    ('Steel', 'Steel'),
    ('Aluminum', 'Aluminum'),
    ('Multi Piece', 'Multi Piece'),
    ('Forged', 'Forged'),
    
    
)

class AdFilterWheels(django_filters.FilterSet):
	location = django_filters.CharFilter(label='<b>Location</b>',lookup_expr='icontains')
	wheel_type = django_filters.MultipleChoiceFilter(choices=WHEEL_TYPE_CHOICES,
                                                   widget=forms.CheckboxSelectMultiple,
                                                   label='<b>Wheel Type</b>')
                                                   
	wheel_color = django_filters.CharFilter(label='<b>Wheel Color</b>',lookup_expr='icontains')
    
	specials = django_filters.MultipleChoiceFilter(choices=Specials_Choices,widget=forms.CheckboxSelectMultiple,label='<b>Special Offers</b>')   
	
	class Meta:
		model = Ad
		fields = ['location','wheel_type','wheel_color','specials']
      





















