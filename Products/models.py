from typing import Any
from django.db import models
from django.contrib.auth.models import User

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

# class Cart(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Cart of {self.user.username}"

# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     added_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.quantity} of {self.product.name} in {self.cart.user.username}'s cart"

#     def get_total_price(self):
#         return self.quantity * self.product.prize
