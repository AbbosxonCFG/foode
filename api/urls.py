from django.urls import path
from .views import *

urlpatterns = [
    path('get-categories/', get_categories),
    path('get-products/', get_products),
    path('create-order/', create_order),
    path('get-cart/', get_cart)
]
