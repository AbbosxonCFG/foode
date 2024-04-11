from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(User)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(AboutUs)
admin.site.register(Stol)
admin.site.register(Cart)
admin.site.register(Waiter)
