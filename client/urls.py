from django.urls import path
from .views import *


urlpatterns=[
    # path("",index,name='index'),
    path("<int:id>/",category_client, name='category_client'),
    path("<int:id>/category/<int:pk>/",product_detail_client,name="product_detail_client"),
    path('about_us',about_us,name="about_us"),
    path('create_cart/<int:id>/<int:pk>/',create_cart,name='create_cart'),
    path('reduce_cart/<int:id>/<int:pk>/',reduce_cart,name='reduce_cart'),
    path("<int:id>/get_cart/",get_cart,name='get_cart'),
    path('del_cart/<int:id>/',del_cart,name='del_cart'),
    path('del_cart/<int:id>/<int:pk>/',del_cart_pk,name='del_cart_pk'),
    path('test/<int:id>/',test,name='test')

]
