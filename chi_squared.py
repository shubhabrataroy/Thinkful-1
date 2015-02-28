# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 22:35:49 2015

@author: mdblr
"""
import pandas as pd
from scipy import stats as stats
import collections
import matplotlib.pyplot as plt

#load the data into Pandas
spark = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

#cleans the data by removing rows with null values
spark.dropna(inplace=True)


freq = collections.Counter(spark['Open.CREDIT.Lines'])
plt.figure()
plt.bar(freq.keys(), freq.values(), width=1)
plt.show

#execute chi-squared test & print result
chi, p = stats.chisquare(freq.values())
print "Chi result: > " + str(chi)
print "p result: > " + str(p)