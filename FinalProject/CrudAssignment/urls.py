# -*- coding: utf-8 -*-
"""
Created on Wed Nov 7 21:49:55 2018

@author: Umar Bin Khalid
"""


from django.conf.urls import url,include

from . import views

app_name = 'CrudAssignment'
urlpatterns = [

    url(r'^$',views.index, name='index'),
    url(r'^create/$',views.create, name='create'),
    url(r'^retrieve/$',views.retrieve, name='retrieve'),
    url(r'^update/$',views.update, name='update'),
    url(r'^delete/$',views.delete, name='delete')


]
