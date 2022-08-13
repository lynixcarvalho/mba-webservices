from django.urls import path

from . import views

urlpatterns = [
    # Get
    path('cliente_lista/', views.cliente_lista, name='cliente_lista'),
    path('cliente_search/', views.cliente_search, name='cliente_search'),
    path('cliente_search/<str:cliente_id>', views.cliente_search_id, name='cliente_search_id'),
    # Post
    path('cliente_create/', views.cliente_create, name='cliente_create'),
    path('cliente_delete/', views.cliente_delete, name='cliente_delete'),
    # Put / Patch
    path('cliente_update/', views.cliente_update, name='cliente_update'),
]
