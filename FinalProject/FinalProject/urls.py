# -*- coding: utf-8 -*-
"""
Created on Wed Nov 7 21:49:55 2018

@author: Umar Bin Khalid
"""

"""
FinalProject URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^", include("CrudAssignment.urls",namespace="CrudAssignment")),

]
