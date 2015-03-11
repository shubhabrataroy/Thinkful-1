# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:38:47 2015

@author: mdblr

"""

import pandas as pd
import statsmodels.api as sm
import math
#import numpy as np
#import matplotlib.pyplot as plt
#from scipy import stats as stats 

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

IntR = []
D = loans_data['Interest.Rate'].tolist() 
for j in range(len(D)):
    if float(D[j]) <= float(12): 
        R = True
    else: 
        R = False 
    IntR.append(R)    
    
loans_data['Less.Than.12']=IntR

loans_data['Intercept'] = 1.0

ind_vars = ['FICO.Score','Amount.Requested','Intercept']

logit = sm.Logit(loans_data['Less.Than.12'], loans_data[ind_vars])
result = logit.fit()

coeff = result.params

LTT_T= loans_data[loans_data['Less.Than.12'] == True]

E= loans_data['Interest.Rate'].tolist()
F= LTT_T['FICO.Score'].tolist()
G= LTT_T['Amount.Requested'].tolist()
#x = np.random.randint(1, len(loans_data))
x= i #using i for iteration on line 67

def logical_regression():
    #print 'FICO Score: ', F[x].astype(float)
    #print 'Loan Amount: ', D[x].astype(float)
    #print 'Interest rate: ', E[x].astype(float), '%'
    p= float(1/(1 + math.exp(-60.125 + (0.087423*(F[i])) - (0.000174*(G[i])))))
    #print 'Probability of loan: ', p
    return p 

for i in range(len(LTT_T)):
    if F[i] == 720:
        if G[i] == 10000:
            print logical_regression()
            
logical_regression()