# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 17:43:21 2015

@author: mdblr
"""

import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

#dicing the data into a list of strings
data = data.splitlines()
#data = data.split('\n')

#dicing up lines
data = [i.split(', ') for i in data]

#determining column labels via variable for pandas
columns_britain = data[0]

#determining rows via variable for pandas
data_britain = data[1::]

#creating dataframe for analysis
df = pd.DataFrame(data_britain, columns=columns_britain)

df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print df['Alcohol'].mean()
print df['Alcohol'].median()
print stats.mode(df['Alcohol'])
print (max(df['Alcohol']) - min(df['Alcohol']))
print df['Alcohol'].mean()
print df['Alcohol'].median()

print df['Tobacco'].mean()
print df['Tobacco'].median()
print stats.mode(df['Tobacco'])
print (max(df['Tobacco']) - min(df['Tobacco']))
print df['Tobacco'].var()
print df['Tobacco'].std()
