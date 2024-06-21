from typing import Any
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.urls import reverse
from django.utils import timezone

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
        return self.quantity * self.price



class Order(models.Model):
    username = models.CharField(max_length=50, default='username')
    first_name = models.CharField(max_length=50, default='first_name')
    last_name = models.CharField(max_length=50, default='last_name')
    company_name = models.CharField(max_length=100, default='company_name')
    address = models.TextField(default='Address')
    house_number_street_name = models.CharField(max_length=100, default='House_Number')
    town_city = models.CharField(max_length=50, default='Town/City')
    country = models.CharField(max_length=50, default='Country')
    postcode_zip = models.CharField(max_length=20, default='POstcode')
    mobile = models.CharField(max_length=20, default='Mobile')
    email_address = models.EmailField(default='Email')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default='Total_Price')
    payment_method = models.CharField(max_length=200, default='Card')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    create_account = models.BooleanField(default=True)
   
    
    # ship_to_different_address = models.BooleanField(default=False)


    def calculate_total_price(self):
       
        items = self.orderitem_set.all()
        total_price = sum(item.price * item.quantity for item in items)
        return total_price

       
    def  __str__(self):
        return 'Order {}'.format(self.id)
    
    
    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())    
      


    
    
class OrderItem(models.Model):
   
     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, default='Order')
     product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, default='Product')
     quantity = models.PositiveIntegerField(default='Quantity')
     price = models.DecimalField(max_digits=10, decimal_places=2, default='Price')
     total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
     
    
     def __str__(self):
             return '{}'.format(self.id)
         
     def get_cost(self):
            return self.price * self.quantity
        



















# RESERVE PLACE

# class Carts(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     cart_id = models.CharField(max_length=100, unique=True, default=False)
    
    

# class OrderItem(models.Model):
#     cart = models.ForeignKey(Carts, related_name="OrderItems", on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50, default='first_name')
#     last_name = models.CharField(max_length=50, default='last_name')
#     company_name = models.CharField(max_length=100, blank=True, null=True)
#     address = models.TextField(default=False)
#     house_number_street_name = models.CharField(max_length=100, default=1)
#     town_city = models.CharField(max_length=50, default=1)
#     country = models.CharField(max_length=50, default=1)
#     postcode_zip = models.CharField(max_length=20, default=1)
#     mobile = models.CharField(max_length=20, default=1)
#     email_address = models.EmailField(default=False)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2, default=False)
#     payment_method = models.CharField(max_length=200, default='card')
    

#     def get_absolute_url(self):
#          return reverse("course:verify-payment", kwargs={
#             "ref": self.ref,
#         })