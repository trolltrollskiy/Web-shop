from django.urls import path

from .api_views import *

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('customers/', CustomerListAPIView.as_view(), name='customers_list'),
    path('smartphones/', SmartphoneListAPIView.as_view(), name='smartphones_list'),
    path('smartphones/<str:id>/', SmartphoneDetailAPIView.as_view(), name='smartphone_detail'),
    path('laptops/', LaptopListAPIView.as_view(), name='laptops_list'),
    path('laptops/<str:id>/', LaptopDetailAPIView.as_view(), name='laptop_detail')
]