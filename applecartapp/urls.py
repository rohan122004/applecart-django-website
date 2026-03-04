from django.contrib import admin
from django.urls import path
from applecartapp import views

urlpatterns = [
    path('',views.index, name='index.html'),
    path('buy/',views.buy, name='buy.html')
]
