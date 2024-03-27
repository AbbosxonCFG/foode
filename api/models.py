from typing import Iterable
from django.db import models
from django .contrib.auth .models import AbstractUser
from django.contrib.auth.models import User


class Waiter(models.Model):
    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def active_carts_count(self):
        return self.cart.filter(is_active=True).count()


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to="rasmlar", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product')
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Stol(models.Model):
    number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.number)


class Order(models.Model):
    stol = models.ForeignKey(Stol, on_delete=models.PROTECT, related_name='order')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='order')
    quantity = models.IntegerField()
    all_price = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.stol.number)
    
    def save(self, *args, **kwargs):
        self.quantity=int(self.quantity)
        self.all_price = self.product.price * self.quantity
        super().save(*args, **kwargs)


class AboutUs(models.Model):
    phone = models.CharField(max_length=23)
    Address = models.CharField(max_length=255)
    instagram = models.CharField(max_length=255)
    work_time = models.CharField(max_length=255)

    def __str__(self):
        return self.Address


class Cart(models.Model):
    waiter = models.ForeignKey(Waiter, on_delete=models.PROTECT, related_name='cart')
    products = models.ManyToManyField(Product, blank=True)
    stol = models.ForeignKey(Stol, on_delete=models.PROTECT, related_name='carts')
    is_active = models.BooleanField(default=True)
    total_price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stol.id

    def save(self, *args, **kwargs):
        super(Cart, self).save(*args, **kwargs)
        if self.products:
            for a in self.products.all():
                self.total_price += a.all_price
            super(Cart, self).save(*args, **kwargs)

  

