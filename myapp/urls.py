from django.urls import path

from .views import *

urlpatterns = [
    path('', root),
    path('products/', ProductsList.as_view(), name='myapp/product_list_url'),
    path('product/create/', ProductCreate.as_view(), name='product_create_url'),
    path('product/<str:slug>/', ProductDetail.as_view(), name='product'),
    path('product/<str:slug>/update/', ProductUpdate.as_view(), name='product_update_url'),
    path('tags/', TagsList.as_view(), name='myapp/tags_list_url'),
    path('tag/create/', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url')
]
