import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class Waiter(models.Model):
    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def active_carts_count(self):
        return self.cart.filter(is_active=True).count()
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.id} {self.name}"





class Stol(models.Model):
    number = models.IntegerField()
    qr = models.ImageField(upload_to="table/", null=True, blank=True)

    def __str__(self):
        return str(self.number)

    def generate_qr(self, link):
        if not self.qr:  # Check if QR image already exists
            qr_image = qrcode.make(link)
            qr_offset = Image.new('RGB', (310, 310), 'white')
            draw_img = ImageDraw.Draw(qr_offset)
            qr_offset.paste(qr_image)
            file_name = f'{self.id}qr.png'
            stream = BytesIO()
            qr_offset.save(stream, 'PNG')
            self.qr.save(file_name, File(stream), save=True)
            self.save()
            qr_offset.close()


class Order(models.Model):
    stol = models.ForeignKey(Stol, on_delete=models.CASCADE, related_name='order')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order')
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
    # waiter = models.ForeignKey(Waiter, on_delete=models.CASCADE, related_name='cart')
    quantity=models.IntegerField()
    product = models.ForeignKey(Product, blank=True ,on_delete=models.CASCADE,related_name='cart')
    stol = models.ForeignKey(Stol, on_delete=models.CASCADE, related_name='cart')
    # is_active = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True,unique=True)

    def __str__(self):
        return str(self.stol.number)

    

  

