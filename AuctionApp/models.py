from django.db import models
from django.contrib.auth.models import User
from time import time
from django.core.validators import RegexValidator


# Create your models here.


def getImage(instance, filename):
    return "AuctionSystem/image_{0}_{1}".format(str(time()), filename)


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=getImage)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    minimum_price = models.IntegerField(null=True)
    selling_price = models.IntegerField(null=False)
    bid_end_date = models.DateTimeField(default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.product_name


class Seller(models.Model):
    user_name = models.ForeignKey(User)
    product_id = models.ForeignKey(Product)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.user_name)


class Bidder(models.Model):
    user_name = models.ForeignKey(User)
    product_id = models.ForeignKey(Product)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    numeric = RegexValidator(r'^[0-9]*$', 'Only numerics are allowed.')
    bid_amount = models.CharField(max_length=100, validators=[numeric])

    def __unicode__(self):
        return str(self.user_name)

