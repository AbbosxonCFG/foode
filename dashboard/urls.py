from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('table/', table, name='table'),
    path('table_delete/<int:pk>/', table_delete, name='table_delete'),
    path('product/',product,name='product'),
    path('product_add/',product_add,name='product_add'),
    path('product_detail/<int:pk>/',product_detail,name='product_detail'),
    path('product_edit/<int:pk>/',product_edit,name='product_edit'),
    path('product_delete/<int:pk>/',product_delete,name='product_delete'),
    path('stol/',stol,name='stol'),
    path('cart/<int:pk>/',cart,name='cart'),
    path('order_delete/<int:pk>/',order_delete,name='order_delete'),
    path('categories/',category,name='category'),
    path('category_add/',category_add,name='category_add'),
    path('category_delete/<int:pk>/',category_delete,name='category_delete')
    
]



