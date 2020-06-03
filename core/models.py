from django.db import models

from accounts.models import User
from django.utils.translation import pgettext_lazy
from django.db.models import F, Max, Q

Condition= [
    ('New','New'),
    ('Used','Used'),
]
Rims= [
    ('Yes','Yes'),
    ('No','No'),
]
Rent= [
    ('Buy','Buy'),
    ('Sell','Sell'),
]
Seasonality= [
    ('Winter','Winter'),
    ('Summer','Summer'),
    ('All-Seasons','All-Seasons'),
]

wheels= [
    ('Bridgestone','Bridgestone'),
    ('Appollo','Appollo'),
    ('Firestun','Firestun'),
    ('Racewheel','Racewheel'),
]

    
class Tyres(models.Model):
    
    Add_Title = models.CharField(max_length=100)
    Tire_Condition = models.CharField(max_length=50, choices=Condition)
    On_Rims = models.CharField(max_length=50, choices=Rims)
    #additional fields
    Year = models.IntegerField()
    Make = models.CharField(max_length=250)
    Model = models.CharField(max_length=250)
    Width = models.IntegerField()
    Ratio = models.IntegerField()
    Diameter = models.IntegerField()
    Tyres_Available = models.IntegerField()
    Rent_Type = models.CharField(max_length=250,choices=Rent)
    #---
    Seasonality= models.CharField(max_length=50, choices=Seasonality)

    def __str__(self):
        return self.Add_Title

class Wheels(models.Model):
    Add_Title = models.CharField(max_length=100)
    Wheels_Brand = models.CharField(max_length=50, choices=wheels)
    #additional fields
    Width = models.IntegerField(default =0)
    Ratio = models.IntegerField(default =0)
    Diameter = models.IntegerField(default =0)
    #---
    Offer_Price = models.CharField(max_length=50)
    Seasonality= models.CharField(max_length=50, choices=Seasonality)

def __str__(self):
        return self.Add_Title
        
class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=255)
    description = models.TextField(verbose_name="Category description")
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    validity = models.IntegerField(default=1)
    imagescount = models.IntegerField(default=1)
    image = models.ImageField(verbose_name="Category Image", upload_to="category_images",
                              default="category_images/default.png")

    def __str__(self):
        return self.title

class AdType(models.Model):
    name = models.CharField(max_length=128)
    has_attributes = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

        
class Ad(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE,  default=1)
    tyre = models.ForeignKey(Tyres, on_delete=models.CASCADE,null=True,default=1)
   # Wheels = models.ForeignKey(Wheels, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255, verbose_name="Ad title")
    price = models.IntegerField(verbose_name="Ad price")
    featured = models.BooleanField(default=False)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    location = models.TextField(null=True, blank=True)
    is_negotiable = models.BooleanField(default=False)
    published_on = models.DateTimeField(auto_now=True)
    is_viewed = models.BooleanField(default=False)
    description = models.TextField(verbose_name="Ad description")
    

    def __str__(self):
        return self.title

    @property
    def first_image_or_default(self):
        return self.ad_images.all()[0].image.url if self.ad_images.count() > 0 else "/media/ad_images/block3.jpg"

    @property
    def ad_status(self):
        if self.status == 1:
            return 'active'
        elif self.status == 2:
            return 'inactive'
        elif self.status == 3:
            return 'sold'
        else:
            return 'deleted'


class AdImage(models.Model):
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="ad_images")
    image = models.ImageField(verbose_name="Ad image", upload_to="ad_images")

class AttributeInputType:
    """The type that we expect to render the attribute's values as."""

    DROPDOWN = "dropdown"
    MULTISELECT = "multiselect"

    CHOICES = [
        (DROPDOWN, pgettext_lazy("Attribute input type", "Dropdown")),
        (MULTISELECT, pgettext_lazy("Attribute input type", "Multi Select")),
    ]

    # list the input types that cannot be assigned to a variant
    NON_ASSIGNABLE_TO_VARIANTS = [MULTISELECT]
    
class BaseAssignedAttribute(models.Model):
    assignment = None
    values = models.ManyToManyField("AttributeValue")

    class Meta:
        abstract = True

    @property
    def attribute(self):
        return self.assignment.attribute

    @property
    def attribute_pk(self):
        return self.assignment.attribute_id


class AssignedAdAttribute(BaseAssignedAttribute):
    """Associate a product type attribute and selected values to a given product."""

    ad = models.ForeignKey(
        Ad, related_name="attributes", on_delete=models.CASCADE
    )
    assignment = models.ForeignKey(
        "AttributeAd", on_delete=models.CASCADE, related_name="adassignments"
    )

    class Meta:
        unique_together = (("ad", "assignment"),)

class AttributeAd(models.Model):
    name = models.CharField(max_length=255, verbose_name="attribute name")
    attribute = models.ForeignKey(
        "Attribute", related_name="attributeAd", on_delete=models.CASCADE
    )
    ad_type = models.ForeignKey(
        AdType, related_name="attributead", on_delete=models.CASCADE
    )
    assigned_products = models.ManyToManyField(
        Ad,
        blank=True,
        through=AssignedAdAttribute,
        through_fields=["assignment", "ad"],
        related_name="attributesrelated",
    )
    
class Attribute(models.Model):
    name = models.CharField(max_length=256, null=True, blank=True)
    input_type = models.CharField(
        max_length=50,
        choices=AttributeInputType.CHOICES,
        default=AttributeInputType.DROPDOWN,
    )

    ad_types = models.ManyToManyField(
        AdType,
        blank=True,
        related_name="ad_attributes",
        through=AttributeAd,
        through_fields=["attribute", "ad_type"],
    )
    is_required = models.BooleanField(default=False)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class SortableModel(models.Model):
    sort_order = models.IntegerField(editable=False, db_index=True, null=True)

    class Meta:
        abstract = True

    def get_ordering_queryset(self):
        raise NotImplementedError("Unknown ordering queryset")

    def get_max_sort_order(self, qs):
        existing_max = qs.aggregate(Max("sort_order"))
        existing_max = existing_max.get("sort_order__max")
        return existing_max

    def save(self, *args, **kwargs):
        if self.pk is None:
            qs = self.get_ordering_queryset()
            existing_max = self.get_max_sort_order(qs)
            self.sort_order = 0 if existing_max is None else existing_max + 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.sort_order is not None:
            qs = self.get_ordering_queryset()
            qs.filter(sort_order__gt=self.sort_order).update(
                sort_order=F("sort_order") - 1
            )
        super().delete(*args, **kwargs)

        
class AttributeValue(SortableModel):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100, blank=True, default="")
    attribute = models.ForeignKey(
        Attribute, related_name="values", on_delete=models.CASCADE
    )

    
    class Meta:
        ordering = ("sort_order", "id")
        
    def __str__(self):
        return self.name

    @property
    def input_type(self):
        return self.attribute.input_type

    def get_ordering_queryset(self):
        return self.attribute.values.all()




