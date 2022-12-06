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

class dataFormation(object):
    def __init__(self, fileName):
        dataBank = pd.read_csv(fileName)
        dataBank = dataBank.dropna(axis='columns', how='all')
        dataBank = dataBank.replace(np.NaN,0)
        dataBank = dataBank.drop(['Country Code', 'Indicator Name', 'Indicator Code'], axis=1) 
        
        self.dataCountries = dataBank
        
        dataBank_t = pd.DataFrame.transpose(dataBank)
        dataBank_t = dataBank_t.rename(index={"Country Name":"Year"})
        dataBank_t.columns = dataBank_t.iloc[0]
        dataBank_t = dataBank_t.iloc[1:]
        
        
        self.dataYears =  dataBank_t
        
    def data_countries(self):
        return self.dataCountries
    
    def data_years(self):
        return self.dataYears
    
    
data_co2 = dataFormation("CO2 emissions (kt).csv")
data_energy = dataFormation("Energy use (kg of oil equivalent per capita).csv")

# print(data_co2.data_countries())
print(data_co2.data_years())