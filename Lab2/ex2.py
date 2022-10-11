import numpy as np
from random import *
from scipy import stats
import arviz as az
import matplotlib.pyplot as plt

np.random.seed(1)

# random 
# arvis_discret
z=[]
nr=0

for i in range(10000):
    y=randint(1,100)
    latenta = stats.expon.rvs(0,0.25,1)
    if y<=25:
        m = stats.gamma.rvs(4,0,1,0.333)
    elif y<=50 and y>25:
        m = stats.gamma.rvs(4,0,1,0.5)
    elif y>50 and y<=80:
        m = stats.gamma.rvs(5,0,1,0.5)
    else:
        m= stats.gamma.rvs(5,0,1,0.333)
    z.append(m+latenta)

    if m+latenta >= 3:
        nr+=1

print("probabilitatea ca timpul sa fie peste 3 este:", nr/10000)

az.plot_posterior({'z':z})
plt.show() 


