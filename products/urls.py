from django.urls import path
from products.views import *
app_name = 'products'

urlpatterns = [
 path('product/<int:pk>/', product, name='product'),
 path('category/<str:pk>/', category, name='category'),
]
