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
import matplotlib as mpl
# =============================================================================
# dataFormation is a class used to extract data from csv file and return data
# =============================================================================
class dataFormation:
    '''
    this class is used to data filter reading the csv file name and return the
    data frames
    '''
    def __init__(self, fileName):
        '''
        this menthod is used to data filter and and assign values to object
        
        Parameters
        ----------
        fileName : CSV file
            fileName is used for data extraction and further which is used for
            setting the data as columns(as countries and years).

        Returns
        -------
        None.

        '''
        dataBank = pd.read_csv(fileName) # readign the data file
        # dropping the na values
        dataBank = dataBank.dropna(axis = 'columns', how = 'all')
        # setting the values to drop
        toDrop = ['Country Code', 'Indicator Name', 'Indicator Code']
        dataBank = dataBank.drop(toDrop, axis = 1) # dropping the values
        # setting the dataFrame values to a variable(countries as columns)
        self.dataCountries = dataBank
        # data frame transpose to get years as columns 
        dataBank_t = pd.DataFrame.transpose(dataBank)
        # changing the country name to year
        dataBank_t = dataBank_t.rename(index = {"Country Name":"Year"})
        dataBank_t = dataBank_t.reset_index() # resetting the index
        dataBank_t.columns = dataBank_t.iloc[0] # setting columns names
        dataBank_t = dataBank_t.iloc[1:] # removing the duplicate row
        # setting the dataFrame values to a variable(years as columns)
        self.dataYears =  dataBank_t
        
    # method to retun data with columns as country names
    def data_countries(self):
        '''
        this method is used to return data frame

        Returns
        -------
        TYPE
            returning data frame with coloumns as countries.

        '''
        return self.dataCountries
    
    # method to retun data with columns as years
    def data_years(self):
        '''
        this method is used to return data frame 

        Returns
        -------
        TYPE
            returning data frame with coloumns as years.

        '''
        return self.dataYears
    
# =============================================================================
# line plot function
# =============================================================================
def linePlot(data, countries, Title):
    '''
    this funcion is used to plot the line plot

    Parameters
    ----------
    data : dataFrame
        used to plot the line plot.
    countries : List
        Counties is a list which is used to plot the data and set the legend.
    Title : String
        a string used as a title for plot.

    Returns
    -------
    None.

    '''
    imageName = Title+" line_Plot.png" # setting the image name
    data.plot('Year', countries,
              label= countries, 
              kind = "line", title = Title)
    plt.grid() # applying grid for the plot to refere the values
    plt.title(Title, size = 35) # setting title for plot and its size
    plt.savefig(imageName) # to save the plots
    plt.show() # to display the plots
    
    return
    
# =============================================================================
# bar plot function
# =============================================================================
def barPlot(data, countries, years, Title):
    '''
    this funcion is used to plot the bar plot

    Parameters
    ----------
    data : dataFrame
        used to plot the bar plot.
    countries : List
        Counties is a list which is used to plot the data and set the legend
    years : list
        this value is used to extract the required data for plotting.
    Title : String
        a string used as a title for plot.

    Returns
    -------
    None.

    '''
    imageName = Title+" bar_plot.png" # setting the image name
    # extract countries of interest
    df_plot = data.loc[data['Country Name'].isin(countries)]
    # plotting bar plot
    df_plot.plot('Country Name', years,
              label= years, 
              kind = "bar", title = Title)
    plt.title(Title, size = 35) # setting title for plot and its size
    plt.grid() # applying grid for the plot to refere the values
    plt.savefig(imageName) # to save the plots
    plt.show() # to display the plots
    
    return

# =============================================================================
# pie plot function
# =============================================================================
def piePlot(data, countries, Title, year):
    '''
    this funcion is used to plot the pie plot

    Parameters
    ----------
    data : dataFrame
        used to plot the line plot.
    countries : List
        Counties is a list which is used to plot.
    Title : String
        a string used as a title for plot.
    year : String
        this value is used to extract the required data.

    Returns
    -------
    None.

    '''
    imageName = Title+" "+year+" pie_plot.png" # setting image name
    # extract countries of interest
    df_plotPie = data.loc[data['Country Name'].isin(countries)]
    # extract year of interest
    df_plotPie = df_plotPie[["Country Name", year]]
    # converting data to numeric    
    df_plotPie[year] = pd.to_numeric(df_plotPie[year])
    # plotting pie plot
    plt.pie(df_plotPie[year], labels = countries)
    plt.title(Title+' '+year, size = 35) # setting title and its size
    plt.savefig(imageName) # to save the plots
    plt.show() # to display the plots
    
    return

# =============================================================================
# invoking the dataFormation funciton to set the values
# expcted vaules to pass - file name
# =============================================================================
data_co2 = dataFormation("CO2 emissions (kt).csv")
data_energy = dataFormation("Energy use (kg of oil equivalent per capita).csv")
data_forest = dataFormation("Forest area (% of land area).csv")
data_mortality = dataFormation("Mortality rate.csv")
data_greenhouse_gas = dataFormation("greenhouse gas emissions.csv")

# setting the values of countries(interested)
county_list = ['Bolivia', 'Denmark', 'Finland', 'Greece', 'Switzerland']
# setting the values of years(interested)
years_list = ['1995', '2000', '2005', '2010', '2015']
# setting the font size to default
mpl.rcParams['font.size'] = 25

# =============================================================================
# invoking line plot function
# expected values to pass dataFrame, county list, title
# =============================================================================
# line plot for CO2 emissions
linePlot(data_co2.data_years(),
          county_list, 
          "CO2 emissions (kt)")
# line plot for Energy use
linePlot(data_energy.data_years(), 
          county_list, 
          "Energy use (kg of oil equivalent per capita)")

# =============================================================================
# invoking bar plot function
# expected values to pass dataFrame, county list, years list, title
# =============================================================================
# bar plot for Total greenhouse gas emissions
barPlot(data_greenhouse_gas.data_countries(), 
        county_list, 
        years_list,
        "Total greenhouse gas emissions (kt of CO2 equivalent)")
# bar plot for Mortality rate, neonatal
barPlot(data_mortality.data_countries(), 
        county_list, 
        years_list,
        "Mortality rate, neonatal (per 1,000 live births)")

# =============================================================================
# invoking pie plot function
# expected values to pass dataFrame, county list, title, year to plot data
# =============================================================================
# pie plot for the year 2005
piePlot(data_co2.data_countries(), 
        county_list,
        "CO2 emissions (kt)", 
        "2005")
# pie plot for the year 2014
piePlot(data_co2.data_countries(), 
        county_list,
        "CO2 emissions (kt)", 
        "2014")
