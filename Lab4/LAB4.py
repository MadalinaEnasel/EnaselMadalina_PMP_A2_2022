from random import randint

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pymc3 as pm
import arviz as az

model = pm.Model()

with model:
    clienti = pm.Poisson("nr. Clienti", mu=20)
    list_t_plata = []
    list_t_preparare = []

    for i in range(0, clienti):
        t_plata = pm.Normal('t_plata', mu=1, sigma=0.5)
        alfa = randint(5, 30)
        t_prepare = pm.Exponential("t_prepare", alfa)
        list_t_plata.append(t_plata)
        list_t_preparare.append(t_prepare)
