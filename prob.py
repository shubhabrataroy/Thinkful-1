# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 17:38:32 2015

@author: mdblr
"""
import collections 
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats as stats

#data
x = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

#outputs frequencies
y = collections.Counter(x)
print x
count_sum = sum(y.values())
for k,v in y.iteritems():
    print "The frequence of number " + str(k) + "is " + str(float(v)/ count_sum)

#boxplot
plt.figure()
plt.boxplot(x)
plt.savefig("Boxplot_x.png")

#histogram
plt.figure()
plt.hist(x, histtype='bar')
plt.savefig("histogram_x.png")

#qq plot
plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.savefig("QQ_test1.png")

