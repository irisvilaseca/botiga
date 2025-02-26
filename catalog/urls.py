from django.urls import path
from . import views

urlpatterns = [
    # Listar todos los productos
    path('products/', views.product_list, name='product_list'),

    # Crear un nuevo producto
    path('products/create/', views.product_create, name='product_create'),

    # Editar un producto existente
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),

    # Eliminar un producto
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
]
