# from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.home),
    path('', views.set_session),
    # path('get/', views.get_cookies),
    path('get/', views.get_session),
    # path('del/', views.delete_cookies),
    path('del/', views.delete_session),
]
