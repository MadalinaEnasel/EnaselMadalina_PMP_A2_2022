import csv
import arviz as az
import pandas as pd

import pymc3 as pm
import numpy as np
from math import log
import matplotlib.pyplot as plt
from scipy import stats
from numpy import exp

p = []
pret = []
x1 = []
x2 = []

data = pd.read_csv('Prices.csv')

for row in data:
    pret.append(data['Price'])
stPret = stats.tstd(pret)

for row in data:
    x1.append(data['Speed'])
stX1 = stats.tstd(x1)
for row in data:
    x2.append(data['HardDrive'])
stX2 = stats.tstd(x2)

with pm.Model() as m_x1x2:
    a = pm.Normal('α', mu=0, sd=10 * stPret)
    b1 = pm.Normal('β1', mu=0, sd=stPret / stX1)
    b2 = pm.Normal('β2', mu=0, sd=stPret / stX2)
    e = pm.HalfCauchy('ε', 5)
    n = a + b1 * x1[:, 0] + b2 * x2[:, 1]
    y_pred = pm.Normal('y_pred', mu=n, sd=e, observed=pret)
    idata_x1x2 = pm.sample(2000, return_inferencedata=True, init='map')
