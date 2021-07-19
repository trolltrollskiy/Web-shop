from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from ..models import *


class CategoryPagination(PageNumberPagination):

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class CategoryListAPIView(ListAPIView, RetrieveUpdateDestroyAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPagination
    lookup_field = 'id'


class SmartphoneListAPIView(ListAPIView, RetrieveUpdateDestroyAPIView):

    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']


class SmartphoneDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = SmartphoneSerializer
    queryset = Smartphone.objects.all()
    lookup_field = 'id'


class LaptopListAPIView(ListAPIView):

    serializer_class = LaptopSerializer
    queryset = Laptop.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['price', 'title']


class LaptopDetailAPIView(RetrieveUpdateDestroyAPIView):

    serializer_class = LaptopSerializer
    queryset = Laptop.objects.all()
    lookup_field = 'id'


class CustomerListAPIView(ListAPIView, RetrieveUpdateDestroyAPIView):

    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = 'id'
