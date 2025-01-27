from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q, Value
from django.forms.models import model_to_dict
from django.utils import timezone
from django.utils.translation import gettext_lazy as _, pgettext_lazy
from django_countries.fields import Country, CountryField
from phonenumber_field.modelfields import PhoneNumber, PhoneNumberField
from .validators import validate_possible_number
#from django.db.models.manager import EmptyManager
from django.db.models.signals import post_save
from django.dispatch import receiver



class PossiblePhoneNumberField(PhoneNumberField):
    """Less strict field for phone numbers written to database."""

    default_validators = [validate_possible_number]




class AddressQueryset(models.QuerySet):
    def annotate_default(self, user):
        # Set default shipping/billing address pk to None
        # if default shipping/billing address doesn't exist
        default_shipping_address_pk, default_billing_address_pk = None, None
        if user.default_shipping_address:
            default_shipping_address_pk = user.default_shipping_address.pk
        if user.default_billing_address:
            default_billing_address_pk = user.default_billing_address.pk

        return user.addresses.annotate(
            user_default_shipping_address_pk=Value(
                default_shipping_address_pk, models.IntegerField()
            ),
            user_default_billing_address_pk=Value(
                default_billing_address_pk, models.IntegerField()
            ),
        )


class Address(models.Model):
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    company_name = models.CharField(max_length=256, blank=True)
    street_address_1 = models.CharField(max_length=256, blank=True)
    street_address_2 = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    city_area = models.CharField(max_length=128, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = CountryField()
    country_area = models.CharField(max_length=128, blank=True)
    phone = PossiblePhoneNumberField(blank=True, default="")

    objects = AddressQueryset.as_manager()

    class Meta:
        ordering = ("pk",)

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    def __str__(self):
        if self.company_name:
            return "%s - %s" % (self.company_name, self.full_name)
        return self.full_name

    def __eq__(self, other):
        if not isinstance(other, Address):
            return False
        return self.as_data() == other.as_data()

    __hash__ = models.Model.__hash__

    def as_data(self):
        """Return the address as a dict suitable for passing as kwargs.

        Result does not contain the primary key or an associated user.
        """
        data = model_to_dict(self, exclude=["id", "user"])
        if isinstance(data["country"], Country):
            data["country"] = data["country"].code
        if isinstance(data["phone"], PhoneNumber):
            data["phone"] = data["phone"].as_e164
        return data

    def get_copy(self):
        """Return a new instance of the same address."""
        return Address.objects.create(**self.as_data())

Type= [
    ('Business Account','Business Account'),
    ('Personal Account','Personal Account'),
]

class User(AbstractUser):
    username = models.CharField(
        'username',
        max_length=50,
        unique=True,
        help_text='Required. 50 characters or fewer. Letters, digits and @/./+/-/_ only.',
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    #about = models.TextField(blank=True)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    addresses = models.ManyToManyField(
        Address, blank=True, related_name="user_addresses"
    )
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    
    phone_number = models.CharField(max_length=12, blank=True, verbose_name="Contact number")
    address = models.CharField(max_length=256, blank=True, verbose_name="address number")
    profile_image = models.ImageField(verbose_name="Profile Picture", upload_to="user_images", blank=True)
    Account_type = models.CharField(max_length=50, choices=Type)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    #objects = GroupManager()

    def __unicode__(self):
        self.fields['phone_number'].required
        return self.email
        
   
        

        
class Questions(models.Model):
    STUDENT_CHOICES = ((True, 'Yes'), (False, 'No'))
    SENIOR_CHOICES = ((True, 'Yes'), (False, 'No'))
    ERSM_CHOICES = ((True, 'Yes'), (False, 'No'))
    is_student = models.BooleanField(choices=STUDENT_CHOICES)
    is_senior_citizen = models.BooleanField(choices=SENIOR_CHOICES)
    is_ersm = models.BooleanField(choices=ERSM_CHOICES) 
    student = models.CharField(max_length=25, blank=True)
    senior_age = models.SmallIntegerField()
    student_id = models.ImageField(verbose_name="Student id", upload_to="student_uploads")
    senior_citizen_id = models.ImageField(verbose_name="Senior id", upload_to="senior_uploads") 
    ersm_yes_questions = models.CharField(max_length=125,)
    ersm_no_questions = models.BooleanField()


