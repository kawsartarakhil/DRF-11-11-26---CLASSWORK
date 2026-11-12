from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list_view, name='category-list'),
    path('categories/create/', views.category_create_view, name='category-create'),
    path('categories/<int:pk>/', views.category_view, name='category-detail'),
    path('categories/<int:pk>/update/', views.category_update_view, name='category-update'),
    path('categories/<int:pk>/delete/', views.category_delete_view, name='category-delete'),
    path('products/', views.product_list_view, name='product-list'),
    path('products/create/', views.product_create_view, name='product-create'),
    path('products/<int:pk>/', views.product_view, name='product-detail'),
    path('products/<int:pk>/update/', views.product_update_view, name='product-update'),
    path('products/<int:pk>/delete/', views.product_delete_view, name='product-delete'),
]

