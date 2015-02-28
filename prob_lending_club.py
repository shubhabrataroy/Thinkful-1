# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 22:16:24 2015

@author: mdblr

"""
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats as stats

#loading data into Pandas
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#cleaning data
loansData.dropna(inplace=True)

#box plot
loansData.boxplot(column='Amount.Requested')
plt.show()

#histogram
loansData.hist(column='Amount.Requested')

#QQ plot
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'], dist='norm', plot=plt)
plt.show()

 