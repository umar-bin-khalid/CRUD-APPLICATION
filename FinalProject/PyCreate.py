# -*- coding: utf-8 -*-
"""
Created on Wed Nov 7 21:49:55 2018

@author: Umar Bin Khalid
"""


import pandas as pd


#file for creating new column in the dataset

"""
@author: Umar Bin Khalid
"""

def createData(ColName, ColValues):
    data = pd.read_csv("dataset.csv")

    data[ColName] = ColValues
    data.to_csv('dataset.csv',header=True,index=False)

    return data
