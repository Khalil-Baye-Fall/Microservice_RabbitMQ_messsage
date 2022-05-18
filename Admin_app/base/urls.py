from django.urls import path
from .views import *

urlpatterns = [
    
    path('products/', ProductView.as_view(), name='products'),
    path('update-product/<str:pk>', ProductIdView.as_view(), name='update-product'),
    path('retreive-product/<str:pk>', ProductIdView.as_view(), name='retreive-product'),
    path('delete-product/<str:pk>', ProductIdView.as_view(), name='delete-product')
    
]
