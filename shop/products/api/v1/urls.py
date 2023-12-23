from django.urls import path
from .views import ProductList, ProductDetail, CategoryList, CategoryDetail, ProductListByCategory, ProductListByPrice

urlpatterns = [
    path('product/', ProductList.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('product/product-category/<str:category_slug>/', ProductListByCategory.as_view(), name='product-list-by-category'),
    path('product/price/<int:min_price>/<int:max_price>/', ProductListByPrice.as_view(), name='product-list-by-price'),
    path('category/', CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),

]