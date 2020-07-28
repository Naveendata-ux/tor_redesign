from django import forms
from django.core.exceptions import ValidationError

from core.models import *
from django.utils.translation import pgettext_lazy
from django.forms.widgets import CheckboxSelectMultiple, TextInput, Select


Tire_Conditions = (
    ('','Select Tire Condition'),
    ('New', 'New'),
    ('Used', 'Used'),
    
)

On_Rims = (
    ('','On Rims'),
    ('Yes', 'Yes'),
    ('No', 'No'),
    
)
year_choices = (
     ('','Select Year'),
     ('2020', '2020'),
     ('2019', '2019'),
     ('2018', '2018'),
     ('2017', '2017'),
     ('2016', '2016'),
     ('2015', '2015'),
     ('2014', '2014'),
     ('2013', '2013'),    
     ('2012', '2012'),
     ('2011', '2011'),
     ('2010', '2010'),
     ('2009', '2009'),
     ('2008', '2008'),
     ('2007', '2007'),
     ('2006', '2006'),
     ('2005', '2005'),
     ('2004', '2004'),
     ('2003', '2003'),
     ('2002', '2002'),
     ('2001', '2001'),
     ('2000', '2000'),
     ('1999', '1999'),
     ('1998', '1998'),
     ('1997', '1998'),
     ('1996', '1996'),
     ('1995', '1995'),
     ('1994', '1994'),
     ('1993', '1993'),
     ('1992', '1992'),
     ('1991', '1991'),
     ('1990', '1990'),
     ('1989', '1989'),
     ('1988', '1988'),
     ('1987', '1987'),
     ('1986', '1986'),
     ('1985', '1985'),
     ('1984', '1984'),
     ('1983', '1983'),
     ('1982', '1982'),
     ('1981', '1981'),
     ('1980', '1980'),
     ('1979', '1979'),
     ('1978', '1978'),
     ('1977', '1977'),
     ('1976', '1976'),
     ('1975', '1975'),
     ('1974', '1974'),
     ('1973', '1973'),
     ('1972', '1972'),
     ('1971', '1971'),
    )
    
make_choices = (
('','Select Make'),
('Acura', 'Acura'), 	           
('Alfa Romeo', 'Alfa Romeo'),	 
('Alpine', 'Alpine'),	 
('ARO', 'ARO'),	 
('Aston Martin', 'Aston Martin'),	 
('Audi', 'Audi'),	 
('BAIC', 'BAIC'),	 
('Baojun', 'Baojun'),	 
('Beiqi', 'Beiqi'),	 
('Beiqi Huansu', 'Beiqi Huansu'),	 
('Beiqi Weiwang', 'Beiqi Weiwang'),	 
('Bentley', 'Bentley'),
('BMW', 'BMW'),
('BMW Alpina', 'BMW Alpina'),	 
('Borgward', 'Borgward'),	 
('Bugatti', 'Bugatti'),	 
('Buick', 'Buick'),	 
('BYD',	'BYD'),
('Cadillac', 'Cadillac'),	 
('Changan', 'Changan'),	 
('Changhe', 'Changhe'),	 
('Chery', 'Chery'),	 
('Chevrolet', 'Chevrolet'),	 
('Chrysler', 'Chrysler'),	 
('Ciimo', 'Ciimo'),	 
('Citroën', 'Citroën'),	 
('Cupra', 'Cupra'),	 
('Dacia', 'Dacia'),	 
('Daewoo', 'Daewoo'),	 
('Daihatsu', 'Daihatsu'),	 
('Datsun', 'Datsun'),	 
('Denza', 'Denza'), 
('Dodge', 'Dodge'),	 
('Dongfeng', 'Dongfeng'),	 
('DR', 'DR'),	 
('DS', 'DS'),	 
('Eagle', 'Eagle'),	 
('Enovate', 'Enovate'),	 
('Enranger', 'Enranger'),	 
('Everus', 'Everus'),	 
('FAW', 'FAW'),	 
('FAW Audi', 'FAW Audi'),	 
('FAW Mazda', 'FAW Mazda'),	 
('FAW Toyota', 'FAW Toyota'),	 
('FAW Volkswagen', 'FAW Volkswagen'),	 
('Ferrari', 'Ferrari'),	 
('Fiat', 'Fiat'),	 
('Fisker', 'Fisker'),	 
('Foday', 'Foday'),	 
('Force', 'Force'),	 
('Ford', 'Ford'),	 
('Foton', 'Foton'),	 
('GAC', 'GAC'),	 
('GAC Fiat', 'GAC Fiat'),	 
('GAC Honda', 'GAC Honda'),	 
('GAC Toyota', 'GAC Toyota'),	 
('GAZ', 'GAz'),	 
('Geely', 'Geely'),	 
('Genesis', 'Genesis'),	 
('GEO', 'GEO'),	 
('GMC',	'GMC'), 
('Great Wall', 'Great Wall'),	 
('Haima', 'Haima'),	 
('Haval', 'Haval'),	 
('Hawtai', 'Hawtai'),	 
('Hindustan', 'Hindustan'),	 
('Holden', 'Holden'),	 
('Honda', 'Honda'),	 
('Huanghai', 'Huanghai'),	 
('Huasong', 'Huasong'),	 
('Hummer', 'Hummer'),	 
('Hyundai', 'Hyundai'),	 
('Infiniti', 'Infiniti'),	 
('Isuzu', 'Isuzu'),	 
('Iveco', 'Iveco'),	 
('JAC', 'JAC'),	 
('Jaguar', 'Jaguar'),	 
('Jeep', 'Jeep'),	 
('Jetta', 'Jetta'), 
('Jinbei', 'Jinbei'),	 
('JMC', 'JMC'),	 
('Karry', 'Karry'), 
('Kia', 'Kia'),	 
('Kinglong', 'Kinglong'),	 
('LADA', 'LADA'),	 
('Lamborghini', 'Lamborghini'),	 
('Lancia', 'Lancia'),	 
('Land Rover', 'Land Rover'),	 
('Landwind', 'Landwind'),	 
('LDV', 'LDV'),
('LEVC', 'LEVC'),	 
('Lexus', 'Lexus'),	 
('Lifan', 'Lifan'),	 
('Lincoln', 'Lincoln'),	 
('Lotus', 'Lotus'),
('Luxgen', 'Luxgen'),	 
('Lynk&amp;Co',	'Lynk&amp;Co'), 
('Mahindra', 'Mahindra'),	 
('Maruti', 'Maruti'),	 
('Maserati', 'Maserati'),	 
('Maxus', 'Maxus'),	 
('Maybach', 'Maybach'),	 
('Mazda', 'Mazda'), 
('McLaren', 'McLaren'),	 
('Mercedes-Benz', 'Mercedes-Benz'),
('Mercury', 'Mercury'),	 
('MG', 'MG'),
('MINI', 'MINI'),	 
('Mitsubishi', 'Mitsubishi'),	 
('Mosler', 'Mosler'),	 
('Nio', 'Nio'),	 
('Nissan', 'Nissan'),	 
('Oldsmobile', 'Oldsmobile'),	 
('Opel', 'Opel'),	 
('Panoz', 'Panoz'),	 
('Perodua', 'Perodua'),	 
('Peugeot', 'Peugeot'),	 
('Plymouth', 'Plymouth'),	 
('Polaris',	'Polaris'), 
('Pontiac', 'Pontiac'),	 
('Porsche', 'Porsche'),	 
('Proton', 'Proton'),	 
('Qiantu', 'Qiantu'),	 
('Qiteng', 'Qiteng'),	 
('Qoros', 'Qoros'),	 
('Ram', 'Ram'),	 
('Ravon', 'Ravon'),	 
('Red Flag', 'Red Flag'),	 
('Rely', 'Rely'),	 
('Renault', 'Renault'),	 
('Renault Samsung', 'Renault Samsung'),	 
('Riich', 'Riich'),	 
('Roewe', 'Roewe'), 
('Rolls-Royce', 'Rolls-Royce'),	 
('Rover', 'Rover'),	 
('Saab', 'Saab'),	 
('Saturn', 'Saturn'),	 
('Scion', 'Scion'),	 
('Seat', 'Seat'),	 
('Skoda', 'Skoda'),	 
('Smart', 'Smart'),	 
('Soueast', 'Soueast'),	 
('SsangYong', 'SsangYong'),	 
('Subaru', 'Subaru'),	 
('Suzuki', 'Suzuki'),	 
('TagAZ', 'TagAZ'),	 
('Tata', 'Tata'),	 
('Tesla', 'Tesla'),	 
('Toyota', 'Toyota'),	 
('UAZ', 'UAZ'),	 
('Vauxhall', 'Vauxhall'),	 
('VAZ', 'VAZ'),	 
('Venucia', 'Venucia'),	 
('Victory', 'Victory'),	 
('Volkswagen', 'Volkswagen'),	 
('Volvo', 'Volvo'),	 
('Vortex', 'Vortex'),	 
('Wey', 'Wey'),	 
('Wuling', 'Wuling'),	 
('XPeng', 'XPeng'),
('Yema', 'Yema'),	 
('ZAZ', 'ZAZ'),	 
('Brilliance', 'Brilliance'),
('Zotye','Zotye'),	 
('Zotye Jiangnan', 'Zotye Jiangnan'),	 
('ZX', 'ZX'),
)

Seasonality = (
('','Select Seasonality'),
('All Season','All Season'),
('Summer','Summer'),
('Winter','Winter'),

)

Ad_type = (
('','Select Ad Type'),
('Rent','Rent'),
('Rent to Sell','Rent to Sell'),
('Sell','Sell'),

)

category = (
('','Select Ad Type'),
('1','Tire'),


)

Wheel_type = (
('','Select Wheel Type'),
('Alloy','Alloy'),
('Steel','Steel'),
('Aluminum','Aluminum'),
('Multi Piece','Multi Piece'),
('Forged','Forged')

)

Specials = (
('','Select Offer Type'),
('Limited Time Offer','Limited Time Offer'),
('Seasonal Discounts','Seasonal Discounts'),
('Promotional Discounts','Promotional Discounts'),
('Special Offer','Special Offer')
)

Service_type = (
('','Service Type'),
('Tire Rotation','Tire Rotation'),
('Tire Repair','Tire Repair'),
('Wheel Balancing','Wheel Balancing'),
('Oil Change','Oil Change'),
('Seasonal Tire Change','Seasonal Tire Change')

)
class AdCreateForm(forms.ModelForm):
    Ad_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ad Title','id': 'ad_title',}),error_messages={'invalid': 'Give a suitble name for your Ad!'})
    #category = forms.CharField(initial="Tires",widget=forms.TextInput(attrs={'readonly':'readonly'}))
    description = forms.CharField(max_length=250,widget=forms.Textarea(attrs={'placeholder': 'Description upto 250 words','id': 'description',}),error_messages={'invalid': 'Please fill description field!'})
    offer_price = forms.IntegerField( min_value=0,error_messages={'invalid': 'Please enter offer price!'})
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Location','id':'search_input'}),error_messages={'invalid': 'Please enter location!'})
    Tire_Condition = forms.ChoiceField(choices = Tire_Conditions)
    On_Rims = forms.ChoiceField(label="On Rims?",choices = On_Rims,widget=forms.Select(attrs={'placeholder': 'On Rims','id': 'on_rims'}))
    Make = forms.ChoiceField(choices=make_choices,widget=forms.Select(attrs={'placeholder': 'Select Make','id': 'sel_make',}),error_messages={'invalid': 'Please select a valid Choice for Make!'})
    Year = forms.ChoiceField(choices=year_choices,widget=forms.Select(attrs={'placeholder': 'Select Year','id': 'sel_make',}),error_messages={'invalid': 'Please select a valid Year!'})
    Model = forms.ChoiceField(required=False,widget=forms.Select(attrs={'placeholder': 'Select Model','id': 'sel_model','class':'form-control'}),error_messages={'invalid': 'Please select a valid Model!'})
    Seasonality= forms.ChoiceField(choices=Seasonality,widget=forms.Select(attrs={'placeholder': 'Select Seasonality','id': 'seasonality',}),error_messages={'invalid': 'Please Select valid choice for Seasonality!'})
    tires_available = forms.IntegerField( min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Number of Tires','id': 'tires_available',}),error_messages={'invalid': 'Please enter value for Tyres_Available!'})
    Tenure_offered = forms.IntegerField(label='', min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Tenure Offered','id': 'tires_offered','style': 'display:none;','id': 'business',}),error_messages={'invalid': 'Please enter value for Tenure_offered!'})
    Ad_Type = forms.ChoiceField(choices=Ad_type,widget=forms.Select(attrs={'placeholder': 'Select Ad Type','id': 'purpose',}),error_messages={'invalid': 'Please select valid choice for Ad_Type!'})
    
    class Meta:
        model = Ad
        #exclude = ('tyre','wheels')
        fields = ( 'Ad_title', 'category','Tire_Condition', 'On_Rims','Year','Make','Model', 'Seasonality','location','Ad_Type',
        'tires_available','Tenure_offered','offer_price', 'description')
    
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
                if image.size > 1 * 6024 * 6024:
                    raise ValidationError("Image file too large ( > 1mb )")
        else:
            raise ValidationError("Couldn't read uploaded images")


class WheelCreateForm(forms.ModelForm):
    Ad_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ad Title','id': 'ad_title',}),error_messages={'invalid': 'Give a suitble name for your Ad!'})
    
    description = forms.CharField(max_length=250,widget=forms.Textarea(attrs={'placeholder': 'Description upto 250 words','id': 'description',}),error_messages={'invalid': 'Please fill description field!'})
    offer_price = forms.IntegerField( min_value=0,error_messages={'invalid': 'Please enter offer price!'})
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Location','id':'search_input'}),error_messages={'invalid': 'Please enter location!'})
    
    Make = forms.ChoiceField(choices=make_choices,widget=forms.Select(attrs={'placeholder': 'Select Make','id': 'sel_make',}),error_messages={'invalid': 'Please select a valid Choice for Make!'})
    Year = forms.ChoiceField(choices=year_choices,widget=forms.Select(attrs={'placeholder': 'Select Year','id': 'sel_make',}),error_messages={'invalid': 'Please select a valid Year!'})
    Model = forms.ChoiceField(required=False,widget=forms.Select(attrs={'placeholder': 'Select Model','id': 'sel_model','class':'form-control'}),error_messages={'invalid': 'Please select a valid Model!'})
    
    tires_available = forms.IntegerField( label="No. of Wheels Offered",min_value=0,widget=forms.NumberInput(attrs={'placeholder': 'Number of Wheels','id': 'tires_available',}),error_messages={'invalid': 'Please enter value for Tyres_Available!'})
    
    wheel_type = forms.ChoiceField(required=False,label="Wheel Type",choices=Wheel_type,widget=forms.Select(attrs={'placeholder': 'Select Wheel Type','id':'wheel_type'}),error_messages={'invalid': 'Please select valid choice for Wheel_Type!'})
    wheel_color = forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Wheel Colour','id':'wheel_color'}),error_messages={'invalid': 'Please enter wheel Color!'}) 
    specials = forms.ChoiceField(required=False,choices=Specials,widget=forms.Select(attrs={'placeholder': 'Select Wheel Type','id': 'specials',}),error_messages={'invalid': 'Please select valid choice for Specials!'})
    
    class Meta:
        model = Ad
        #exclude = ('tyre','wheels')
        fields = ( 'Ad_title', 'category','Year','Make','Model', 'location',
        'tires_available','offer_price', 'description','wheel_type','wheel_color','specials')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(WheelCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        self._validate_unique = True
        self.validate_ad_images()
        return self.cleaned_data

    def validate_ad_images(self):
        images = self.request.FILES.getlist('image')
        if images:
            for image in images:
                if image.size > 1 * 6024 * 6024:
                    raise ValidationError("Image file too large ( > 1mb )")
        else:
            raise ValidationError("Couldn't read uploaded images")


class ServicesCreateForm(forms.ModelForm):
    Ad_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Ad Title','id': 'ad_title',}),error_messages={'invalid': 'Give a suitble name for your Ad!'})
    #category = forms.CharField(initial="Services",widget=forms.TextInput(attrs={'readonly':'readonly'}))
    description = forms.CharField(max_length=250,widget=forms.Textarea(attrs={'placeholder': 'Description upto 250 words','id': 'description',}),error_messages={'invalid': 'Please fill description field!'})
    offer_price = forms.IntegerField( min_value=0,error_messages={'invalid': 'Please enter offer price!'})
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Location','id':'search_input'}),error_messages={'invalid': 'Please enter location!'})
    
    
    specials = forms.ChoiceField(required=False,choices=Specials,widget=forms.Select(attrs={'placeholder': 'Select Wheel Type','id': 'specials',}),error_messages={'invalid': 'Please select valid choice for Specials!'})
    
    class Meta:
        model = Ad
        #exclude = ('tyre','wheels')
        fields = ( 'Ad_title','category','location','offer_price','description','specials')
    
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(ServicesCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        self._validate_unique = True
        self.validate_ad_images()
        return self.cleaned_data

    def validate_ad_images(self):
        images = self.request.FILES.getlist('image')
        if images:
            for image in images:
                if image.size > 1 * 6024 * 6024:
                    raise ValidationError("Image file too large ( > 1mb )")
        else:
            raise ValidationError("Couldn't read uploaded images")




   

class AdUpdateForm(forms.ModelForm):
    Ad_title = forms.CharField(error_messages={'invalid': 'Give a suitble name for your Ad!'})
    #category = forms.CharField(error_messages={'invalid': 'Please select a valid Category!'})
   # Width = forms.CharField(error_messages={'invalid': 'Please select a valid Choice!'})
   # Year = forms.ChoiceField(error_messages={'invalid': 'Please select a valid Year!'})
    
    #Aspect_Ratio = forms.CharField(error_messages={'invalid': 'Please select a valid Choice!'})
    
    
    class Meta:
        model = Ad
        fields = ( 'Ad_title', 'description', 'category','offer_price', 'location','Tire_Condition', 'On_Rims','Year','Make','Model','tires_available','Tenure_offered','Ad_Type', 'Seasonality')
        
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
                if image.size > 1 * 5024 * 1024:
                    raise ValidationError("Image file too large ( > 1mb )")
        else:
            raise ValidationError("Couldn't read uploaded images")

class AdImageForm(forms.ModelForm):
    class Meta:
        model = AdImage
        fields = ("image",)

   
