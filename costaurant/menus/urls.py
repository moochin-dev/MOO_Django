from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view),
    path('food/<str:menu>/', views.detail),
]