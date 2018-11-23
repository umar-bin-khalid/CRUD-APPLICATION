# -*- coding: utf-8 -*-
"""
Created on Wed Nov 7 21:49:55 2018

@author: Umar Bin Khalid
"""

from django.shortcuts import render
import pandas as pd

import PyUpdate
import PyDelete
import PyCreate

"""
@author: Umar Bin Khalid
"""
def index(request):
    return render(request, "CrudAssignment/index.html")


"""
@author: Umar Bin Khalid
"""
def update(request):
    key = {}
    nameBefore = str(request.GET.get('oldName'))
    nameNow = str(request.GET.get('newname'))


    if(request.GET.get('updt')):
        key = PyUpdate.UpdateFile( nameBefore, nameNow )
        res = {'updatedResult': key }

        return render(request,"CrudAssignment/update.html",context=res)
    return render(request,"CrudAssignment/update.html")


"""
@author: Umar Bin Khalid
"""
def delete(request):

    name = str(request.GET.get('colName'))
    if (request.GET.get('del')):

        colName =  PyDelete.DeleteFile(name)
        data_to_html = colName.to_html()
        context = {'dataHtml': data_to_html}
        return render(request,"CrudAssignment/delete.html",context)

    return render(request,"CrudAssignment/delete.html")


"""
@author: Umar Bin Khalid
"""
def create(request):

    Name = str(request.GET.get('newname'))
    Value = str(request.GET.get('newval'))

    if (request.GET.get('crt')):
        data = PyCreate.createData(Name,Value)
        data_to_html = data.to_html()
        context = {'dataHtml': data_to_html}
        return render(request,"CrudAssignment/create.html",context)
    return render(request,"CrudAssignment/create.html")


"""
@author: Umar Bin Khalid
"""
def retrieve(request):

    columns = ["REF_DATE","GEO","DGUID","Food categories","Commodity","UOM","UOM_ID","SCALAR_FACTOR","SCALAR_ID","VECTOR","COORDINATE","VALUE","STATUS","SYMBOL","TERMINATED","DECIMALS"]


    data = pd.read_csv('dataset.csv',names=columns)
    data_to_html = data.to_html()
    context = {'dataHtml': data_to_html}
    return render(request, "CrudAssignment/retrieve.html", context)
