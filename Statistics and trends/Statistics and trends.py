# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 22:29:06 2022

Assignment 2: Statistics and trends

Topics choosen for comparision are 
- CO2 emissions (kt)
- Energy use (kg of oil equivalent per capita)

@author: lalit
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class dataFormation:
    def __init__(self, fileName):
        dataBank = pd.read_csv(fileName)
        dataBank = dataBank.dropna(axis='columns', how='all')
        # dataBank = dataBank.replace(np.NaN,0)
        toDrop = ['Country Code', 'Indicator Name', 'Indicator Code']
        dataBank = dataBank.drop(toDrop, axis=1) 
        
        self.dataCountries = dataBank
        
        dataBank_t = pd.DataFrame.transpose(dataBank)
        dataBank_t = dataBank_t.rename(index={"Country Name":"Year"})
        dataBank_t = dataBank_t.reset_index()
        dataBank_t.columns = dataBank_t.iloc[0]
        dataBank_t = dataBank_t.iloc[1:]
        
        self.dataYears =  dataBank_t
        
    def data_countries(self):
        return self.dataCountries
    
    def data_years(self):
        return self.dataYears
    

def linePlot(data, countries):
    # print(data)
    data.plot('Year', countries, label= countries, kind = "line", fontsize = 22)
    # data.plot(xlabel='X Label', ylabel='Y Label', title='Plot Title')
    
    return
    
    
data_co2 = dataFormation("CO2 emissions (kt).csv")
data_energy = dataFormation("Energy use (kg of oil equivalent per capita).csv")

county_list = ['Bolivia', 'Denmark', 'Finland', 'Georgia', 'Switzerland']

# print(data_co2.data_countries())
# print(data_co2.data_years())

linePlot(data_co2.data_years(),county_list)
linePlot(data_energy.data_years(),county_list)