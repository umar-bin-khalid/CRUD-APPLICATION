# -*- coding: utf-8 -*-
"""
Created on Wed Nov 7 21:49:55 2018

@author: Umar Bin Khalid
"""



import pandas as pd

#file for deleting columns in datset
"""
@author: Umar Bin Khalid
"""

def DeleteFile(Name):

    data = pd.read_csv('dataset.csv',low_memory=False)
    data = data.drop(columns=Name)
    return data
