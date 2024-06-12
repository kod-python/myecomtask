from typing import Any
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    updated_on = models.DateField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    CLASSIFICATION_TYPE = (
        ('organic', 'Organic'),
        ('inorganic', 'Inorganic'),
    )
    HEALTH_STATUS = (
        ('healthy', 'Healthy'),
        ('unhealthy', 'Unhealthy'),
    )

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(default=False, blank=True)
    weight = models.DecimalField(max_digits=20, decimal_places=2)
    min_weight = models.DecimalField(max_digits=10, decimal_places=2)
    country_of_origin = models.CharField(max_length=100)
    quality = models.CharField(max_length=25, choices=CLASSIFICATION_TYPE, null=True, blank=True)
    health_status = models.CharField(max_length=25, choices=HEALTH_STATUS, null=True, blank=True)
    classification = models.CharField(max_length=25, choices=CLASSIFICATION_TYPE, null=True, blank=True)
    is_feature = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    is_organic = models.BooleanField(default=False)
    is_inorganic = models.BooleanField(default=False)

    category = models.ForeignKey(Category, related_name="products", blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_total_price(self):
        return self.quantity * self.prize





class Carts(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class OrderItem(models.Model):
    cart = models.ForeignKey(Carts, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, default='first_name')
    last_name = models.CharField(max_length=50, default='last_name')
    company_name = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(default=False)
    house_number_street_name = models.CharField(max_length=100, default=1)
    town_city = models.CharField(max_length=50, default=1)
    country = models.CharField(max_length=50, default=1)
    postcode_zip = models.CharField(max_length=20, default=1)
    mobile = models.CharField(max_length=20, default=1)
    email_address = models.EmailField(default=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=False)
    payment_method = models.CharField(max_length=200, default='card')
    

    def get_absolute_url(self):
         return reverse("course:verify-payment", kwargs={
            "ref": self.ref,
        })