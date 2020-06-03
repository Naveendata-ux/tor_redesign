from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import Group

from .models import User, Address, Questions
from django.forms import ModelForm


class UserRegistrationForm(UserCreationForm):
    
    UserType = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   required=True)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Enter Username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['UserType'].widget.attrs.update({'placeholder': 'Enter UserType'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Enter password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat your password'})
        # self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or 'email@address.nl'

    class Meta:
        model = User
        fields = ("username",
                  "email",
                  "UserType",
                  "password1",
                  "password2",
                  )

    def clean_username(self):
        username = self.cleaned_data['username']
        print(username)
        if ' ' in username:
            raise forms.ValidationError("Username can't contain spaces.")
        return username

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.group = self.cleaned_data['UserType']
        if commit:
            user.save()
        return user

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email',
            'about',
            'phone_number',
            
            
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            
            'profile_image',
        ]
        


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            
            'street_address_1',
        ]

class QuestionsForm(forms.Form):
    STUDENT_CHOICES = ((True, 'Yes'), (False, 'No'))
    SENIOR_CHOICES = ((True, 'Yes'), (False, 'No'))
    ERSM_CHOICES = ((True, 'Yes'), (False, 'No'))
    ERSM_YES_CHOICES = (('CAA', 'CAA'), ('CandianTire', 'CandianTire') , ('others', 'Others'))
    ERSM_NO_CHOICES  = ((True, 'Yes'), (False, 'No'))
    
    is_student = forms.ChoiceField( choices=STUDENT_CHOICES, label = "Are you student", widget=forms.RadioSelect)
    student = forms.CharField(
        label="Student ID",
        widget=forms.TextInput,
    )
    student_id = forms.ImageField()
    is_senior_citizen = forms.ChoiceField( choices=SENIOR_CHOICES,label = "Are you Senior Citizen", widget=forms.RadioSelect)
    is_student = forms.ChoiceField( choices=STUDENT_CHOICES, label = "Are you student", widget=forms.RadioSelect)
    senior = forms.CharField(
        label="Senior Citizen Age",
        widget=forms.TextInput,
    )
    senior_id = forms.ImageField()
    is_ersm = forms.ChoiceField(choices=ERSM_CHOICES, label = "Do you have Emergency Roadside Service Membership ?", widget=forms.RadioSelect)
    ersm_yes_questions = forms.ChoiceField(choices=ERSM_YES_CHOICES, label = "Which service provider?", widget=forms.RadioSelect)
    ersm_no_questions = forms.ChoiceField(choices=ERSM_NO_CHOICES, label = "Would you be interested in ERS?", widget=forms.RadioSelect)
   
    class Meta:
        model = Questions
    
    def save(self, *args, **kwargs):
        QuestionsForm.save(*args, **kwargs)
    
    
        
class UserLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password'})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("User Does Not Exist.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not self.user.is_active:
                raise forms.ValidationError("User is not Active.")

        # return self.cleaned_data
        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user
