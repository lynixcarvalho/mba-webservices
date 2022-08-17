from django.urls import path

from . import views

urlpatterns = [
    # Get
    path('clientes/', views.lista),
    path('clientes/search', views.search),
    path('clientes/search/<str:cliente_id>', views.search_id),
    # Post
    path('clientes/create', views.create),
    path('clientes/delete', views.delete),
    # Put / Patch
    path('clientes/update', views.update),
]
