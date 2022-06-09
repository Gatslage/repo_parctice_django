"""debuterDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('band_list/',view=views.band_list,name='band-list'),
    path('band_details/<int:aId>/',views.band_details,name='band-details'),
    path('contact-us/',views.contactUs,name='contact-us'),
    path('receive/',views.receive,name='receive'),
    path('about-us/',views.aboutUs,name='about-us'),
    path('annonce_list/',views.annonce,name='annonce-list'),
    path('annonce_list/<slug:title>/<int:idBand>/',views.annonce,name='annonce-listG')
]
