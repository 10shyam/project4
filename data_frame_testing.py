# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:55:19 2022

@author: SHYAM SUNDER
"""
def data_frame_test():
    import pandas as pd
     
    # read by default 1st sheet of an excel file
    dataframe1 = pd.read_excel('positions.xlsx', )
     
    return dataframe1