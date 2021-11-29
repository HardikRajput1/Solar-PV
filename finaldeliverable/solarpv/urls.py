# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.hindex),
    
    path('register',views.showRegister),
    path('storeRegister',views.storeRegister),
    path('login',views.showLogin, name="login"),
    
    path('client',views.showClient),
    path('storeClient',views.storeClient),
    
    path('location',views.showLocation),
    path('storeLocation',views.storeLocation),
    
    path('product',views.showProduct),
    path('storeProduct',views.storeProduct),
    
    path('teststandard',views.showTestStandard),
    path('storeTestStandard',views.storeTestStandard),
    
    path('certificate',views.showCertificate),
    path('storeCertificate',views.storeCertificate),
    
    path('tnc',views.showTestingnCertification),
]