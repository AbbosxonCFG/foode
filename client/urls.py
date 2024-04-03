from django.urls import path
from .views import *


urlpatterns=[
    # path("",index,name='index'),
    path("",category_client, name='category_client'),
    path("category/<int:pk>/",product_detail_client,name="product_detail_client"),
    path('about_us',about_us,name="about_us"),
    path('create_order/',create_order,name='order')
    # path("cart/<int:pk/",cart,name='cart')

]