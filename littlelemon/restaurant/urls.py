from django.contrib import admin 
from django.urls import path 
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [ 
    path('', index, name='index'),
    path('menu-items/', MenuItemsView.as_view()),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]