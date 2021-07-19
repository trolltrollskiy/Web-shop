from django.urls import path
from .views import (
    BaseView, ProductDetailView, CategoryDetailView,
    AddToCartView, CartView, DeleteFromCartView,
    ChangeQTYView, CheckoutView, MakeOrderView, comment_view,
    create_comment, create_child_comment )

urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:ct_model>/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:ct_model>/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('comments', comment_view),
    path('create_comment', create_comment, name='comment_create'),
    path('create_child_comment/', create_child_comment, name='comment_child_create')

]