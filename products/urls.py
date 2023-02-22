from django.urls import path
from products.apps import ProductsConfig
from products.views import *

app_name = ProductsConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),

]