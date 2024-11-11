from django.urls import path

from .views import index, contact, layout_static, layout_sidenav

urlpatterns = [
    path('',index),
    path('index.html',index),
    path('contact',contact),
    path('layout-static.html',layout_static),
    path('layout-sidenav-light.html',layout_sidenav),
]