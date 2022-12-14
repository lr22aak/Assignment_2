# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 22:29:06 2022

Assignment 2: Statistics and trends

Topics choosen for comparision are 
- CO2 emissions (kt)
- Energy use (kg of oil equivalent per capita)
- Forest area (% of land area)
- Mortality rate, neonatal (per 1,000 live births)
- Total greenhouse gas emissions (kt of CO2 equivalent)

@author: lalit
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

class dataFormation:
    def __init__(self, fileName):
        dataBank = pd.read_csv(fileName)
        dataBank = dataBank.dropna(axis='columns', how='all')
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
    

def linePlot(data, countries, Title, fontSize):
    # print(data)
    imageName = Title+" line_Plot.png"
    data.plot('Year', countries,
              label= countries, 
              kind = "line", fontsize = fontSize, title = Title)
    plt.grid()
    plt.rc('legend', fontsize=fontSize)
    plt.title(Title, size = 35)
    plt.xlabel('Year',size = fontSize)
    plt.savefig(imageName)
    plt.show()
    
    return
    

def barPlot(data, countries, years, fontSize, Title):
    imageName = Title+" bar_plot.png"
    # extract countries of interest
    df_plot = data.loc[data['Country Name'].isin(countries)]
    
    # df_plot.plot.bar('Country Name', years)
    df_plot.plot('Country Name', years,
              label= countries, 
              kind = "bar", fontsize = fontSize, title = Title)
    plt.title(Title, size = 35)
    plt.ticklabel_format()
    plt.xlabel('Country Names',size = fontSize)
    plt.legend(years)
    plt.savefig(imageName)
    plt.show()
    
    return

def piePlot(data, countries, Title, year):
    imageName = Title+" pie_plot.png"
    # extract countries of interest
    df_plotPie = data.loc[data['Country Name'].isin(countries)]
    df_plotPie = df_plotPie[["Country Name", year]]
    print(df_plotPie)
    # df_1990["1990"] = pd.to_numeric(df_1990["1990"])
    
    
    
    df_plotPie[year] = pd.to_numeric(df_plotPie[year])
    
    plt.pie(df_plotPie[year], labels = countries)
    plt.rc('legend', fontsize=25)
    plt.title(Title+year, size = 35)
    plt.savefig(imageName)
    plt.show()
    return
    
data_co2 = dataFormation("CO2 emissions (kt).csv")
data_energy = dataFormation("Energy use (kg of oil equivalent per capita).csv")
data_forest = dataFormation("Forest area (% of land area).csv")
data_mortality = dataFormation("Mortality rate.csv")
data_greenhouse_gas = dataFormation("greenhouse gas emissions.csv")

county_list = ['Bolivia', 'Denmark', 'Finland', 'Greece', 'Switzerland']
years_list = ['1995', '2000', '2005', '2010', '2015']


# linePlot(data_co2.data_years(),
#           county_list, 
#           "CO2 emissions (kt)",
#           25)

# linePlot(data_energy.data_years(), 
#           county_list, 
#           "Energy use (kg of oil equivalent per capita)",
#           25)

# barPlot(data_greenhouse_gas.data_countries(), 
#         county_list, 
#         years_list, 25,
#         "Total greenhouse gas emissions (kt of CO2 equivalent)")

# barPlot(data_mortality.data_countries(), 
#         county_list, 
#         years_list, 25,
#         "Mortality rate, neonatal (per 1,000 live births)")

piePlot(data_co2.data_countries(), 
        county_list,
        "CO2 emissions (kt)", 
        "2005")

piePlot(data_co2.data_countries(), 
        county_list,
        "CO2 emissions (kt)", 
        "2014")