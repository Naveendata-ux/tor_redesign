from django import forms
from django.core.exceptions import ValidationError

from core.models import *
from django.utils.translation import pgettext_lazy
from django.forms.widgets import CheckboxSelectMultiple, TextInput, Select


class AdCreateForm(forms.ModelForm):
    rent_choices = (
      (1, 'Rent'),
      (3, 'Rent to Own'),
      (5, 'Buy Or Own'),
    )
    year_choices = (
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
    make = forms.ChoiceField(choices=make_choices,
        required=False,
        label=pgettext_lazy("Product Make", "Make"), widget = Select(attrs={
            'id': 'sel_make',}) 
    )
    model = forms.ChoiceField(
        required=False,
        label=pgettext_lazy("Product Model", "Model"), widget = Select(attrs={
            'id': 'sel_model',}) 
    )
    year = forms.ChoiceField(choices=year_choices,
        required=False,
        label=pgettext_lazy("Product Year", "Year"), widget = Select(attrs={
            'id': 'sel_year',}) 
    ) 
    rent_type = forms.ChoiceField(choices=rent_choices,
        required=False,
        label=pgettext_lazy("Product Type", "rent_type"), 
    )
    class Meta:
        model = Ad
        exclude = ("user","year","make","model","rent_type")

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(AdCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        self._validate_unique = True
        #self.validate_ad_images()
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
