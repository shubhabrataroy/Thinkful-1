# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:15:48 2015

@author: mdblr
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm

loans_data = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loans_data.to_csv('loansData_clean.csv', header=True, index=False)

#cleaning RICO.Range data for first value in values
FICO = [] #Creating array for desired values
A = loans_data['FICO.Range'].tolist() #converting column in dataframe to 
for i in range(len(A)): #for loop goes through all rows in data
    B = A[i].split('-') #removes hyphen from str creating two stings
    C = float(B[0]) #converts first str into a float
    FICO.append(C) #appends float to our new array
loans_data['FICO.Score'] = FICO #creates column in data frame from RICO

#cleaning data from Interest.Rate columnn. Need to remove '%' from values and convert to float
loans_data['Interest.Rate'] = loans_data['Interest.Rate'].map(lambda x: x.rstrip('%'))
loans_data['Interest.Rate'] = loans_data['Interest.Rate'].astype(float)

'''#creating variables for our graph from the data
intrate = loans_data['Interest.Rate']
loan_amount = loans_data['Amount.Requested']
fico = loans_data['FICO.Score']

#setting up matrices for graphing
y = np.matrix(intrate).transpose()
x1 = np.matrix(loan_amount).transpose()
x2 = np.matrix(fico).transpose()

creating columns for each array
x = np.column_stack([x1, x2])

creating a linear model using statsmodels.api 
X = sm.add_constant(x)
model = sm.OLS(y, X)
f = model.fit()

print "Coefficients: ", f.params[1:3]
print "Intercept: ", f.params[0]
print "P-values: ", f.pvalues
print "R-Squared: ", f.rsquared'''






