# -*- coding: utf-8 -*-
"""
Created on Wed Nov 7 21:49:55 2018

@author: Umar Bin Khalid
"""


import pandas as pd

"""
@author: Umar Bin Khalid
"""

def UpdateFile(colName,newName):

    data = pd.read_csv('dataset.csv',low_memory=False)

    header = []
    NewNames = []

    header = list(data)

    if colName in header:

        data = data.rename(columns={colName: newName},copy=True)
        NewNames = list(data)
        data.to_csv("dataset.csv", index=False, encoding='utf8',header=True)

        return NewNames
    else:
        print("No column name present")
