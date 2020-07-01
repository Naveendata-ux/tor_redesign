from django.db import models

from accounts.models import User


class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=255)
    image = models.ImageField(verbose_name="Category Image", upload_to="category_images",
                              default="category_images/default.png")

    def __str__(self):
        return self.title


class Ad(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE,  default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    Ad_title = models.CharField(max_length=256, verbose_name="Ad title")
    offer_price = models.PositiveIntegerField(verbose_name="Ad price",default =1)
    featured = models.BooleanField(default=False)
    status = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=256,null=True, blank=True)
    is_negotiable = models.BooleanField(default=False)
    published_on = models.DateTimeField(auto_now=True)
    is_viewed = models.BooleanField(default=False)
    description = models.TextField(verbose_name="Ad description")
    favourite = models.ManyToManyField(User, related_name="favourite", blank=True)
    Tire_Condition = models.CharField(max_length=50)
    On_Rims = models.CharField(max_length=50)
    Year = models.PositiveIntegerField(default =2020)
    Make = models.CharField(max_length=250)
    Model = models.CharField(max_length=250)
    Width = models.PositiveIntegerField(default =1)
    Aspect_Ratio = models.PositiveIntegerField(default =1)
    tires_available = models.PositiveIntegerField(default =1)
    Tenure_offered = models.PositiveIntegerField(default =1)
    Ad_Type = models.CharField(max_length=250)
    Wheels_Brand = models.CharField(max_length=50)
    Seasonality= models.CharField(max_length=50)
    

    def __str__(self):
        return self.Ad_title
    
    @property
    def first_image_or_default(self):
        return self.ad_images.all()[0].image.url if self.ad_images.count() > 0 else "/media/ad_images/default.jpg"
    
    
    
    
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
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name="ad_images" ,default =1)
    image = models.ImageField(verbose_name="Ad image", upload_to="ad_images")
    
class Contact(models.Model):
    Name = models.CharField(max_length=256)
    Email = models.EmailField(max_length=256)
    Subject = models.CharField(max_length=256)
    Message = models.TextField(max_length=256)
    
    def __str__(self):
        return self.Name
    
    
    
    
