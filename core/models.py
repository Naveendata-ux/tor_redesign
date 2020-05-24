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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name="Ad title")
    price = models.IntegerField(verbose_name="Ad price")
    description = models.TextField(verbose_name="Ad description")
    featured = models.BooleanField(default=False)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now=True)
    year = models.CharField(max_length=4, null=True, blank=True)
    make = models.CharField(max_length=50, null=True,blank=True)   
    model = models.CharField(max_length=20, null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    rent_type = models.SmallIntegerField(null=True, default=0)

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
