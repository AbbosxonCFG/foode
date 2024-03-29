from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('table/', table, name='table'),
    path('product/',product,name='product'),
    path('product_add/',product_add,name='product_add'),
    path('product_detail/<int:pk>/',product_detail,name='product_detail'),
    path('product_edit/<int:pk>/',product_edit,name='product_edit'),
    path('product_delete/<int:pk>/',product_delete,name='product_delete'),
    
]



