from django.urls import path

from . import views

urlpatterns = [
    # Get
    path('cartao_lista/', views.cartao_lista, name='cartao_lista'),
    path('cartao_search/', views.cartao_search, name='cartao_search'),
    path('cartao_search/<str:number>', views.cartao_search_number, name='cartao_search_number'),
    # Post
    path('cartao_create/', views.cartao_create, name='cartao_create'),
    path('cartao_delete/', views.cartao_delete, name='cartao_delete'),
    # path('cartao_update/', views.cartao_update, name='cartao_update'),
]