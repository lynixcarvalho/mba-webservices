from django.urls import path

from . import views

urlpatterns = [
    # Get
    path('cartoes/', views.lista),
    path('cartoes/search', views.search),
    path('cartoes/search/<str:number>', views.search_number),
    # Post
    path('cartoes/create', views.create),
    path('cartoes/delete', views.delete),
    # Put / Patch
    path('cartoes/update', views.update),
]
