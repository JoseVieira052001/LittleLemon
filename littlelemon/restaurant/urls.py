from django.contrib import admin 
from django.urls import path 
from .views import *
  
urlpatterns = [ 
    path('', index, name='index'),
    path('menu-items/', MenuItemsView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
]