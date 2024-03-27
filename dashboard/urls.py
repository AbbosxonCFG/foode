from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('table/', table, name='table'),
]



