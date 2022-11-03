import csv
import arviz as az
import pymc3 as pm
import matplotlib.pyplot as plt

x = []
y = []

with open("data.csv", 'r') as file:
    plots = csv.reader(file)
    for row in plots:
        x.append(row[3])
        y.append(row[1])

_, ax = plt.subplots(1, 2, figsize=(8, 4))
ax[0].plot(x, y, 'C0.')
ax[0].set
ax[0].set_xlabel('MomAge')
ax[0].set_ylabel('ppvt', rotation=0)
ax[1].set_xlabel('y')
plt.tight_layout()
plt.show()

with pm.Model() as model_g:
    alfa = pm.Normal('alfa', mu=0, sd=10)
    beta = pm.Normal('beta', mu=0, sd=1)
    epsilon = pm.HalfCauchy('epsilon', 5)
    miu = pm.Deterministic('miu', alfa + beta * x)
    y_pred = pm.Normal('y_pred', mu=miu, sd=epsilon, observed=y)
    idata_g = pm.sample(2000, tune=2000, return_inferencedata=True)