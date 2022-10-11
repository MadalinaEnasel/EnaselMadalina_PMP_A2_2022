import numpy as np
from random import *
from scipy import stats
import arviz as az
import matplotlib.pyplot as plt

np.random.seed(1)

# random 
# arvis_discret
z=[]

for i in range(10000):
    y=randint(1,100)
    if y<=40:
        m = stats.expon.rvs(0,0.25,1)
    else:
        m = stats.expon.rvs(0,0.16,1)
    z.append(m)

az.plot_posterior({'z':z})
plt.show() 


