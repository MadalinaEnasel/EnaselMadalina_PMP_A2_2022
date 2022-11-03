import csv
import arviz as az
# import pymc3 as pm
import matplotlib.pyplot as plt
import stats as stats

x = []
y = []

with open("data.csv", 'r') as file:
    plots = csv.reader(file)
    for row in plots:
        x.append(row[3])
        y.append(row[1])

_, ax = plt.subplots(1, 2, figsize=(8, 4))
ax[0].plot(x, y, 'm.')
ax[0].set
ax[0].set_xlabel('MomAge')
ax[0].set_ylabel('ppvt', rotation=0)
ax[1].set_xlabel('y')
plt.tight_layout()
plt.show()

dev = stats.stds(y)
dev2 = stats.st(x)

with pm.Model() as model_g:
    alfa = pm.Normal('alfa', mu=0, sd=10*dev)
    beta = pm.Normal('beta', mu=0, sd=1*dev/dev2)
    epsilon = pm.HalfCauchy('epsilon', 5)
    miu = pm.Deterministic('miu', alfa + beta * x)
    y_pred = pm.Normal('y_pred', mu=miu, sd=epsilon, observed=y)

idata_g = pm.sample(2000, tune=2000, return_inferencedata=True)
az.plot_trace(idata_g, var_names=['α', 'β', 'ε'])

alpha_m = alfa.mean().item()
beta_m = beta.mean().item()
ppc = pm.sample_posterior_predictive(idata_g, samples=400, model=model_g)
plt.plot(x, y, 'b.')
plt.plot(x, alpha_m + beta_m * x, c='k',
label=f'y = {alpha_m:.2f} + {beta_m:.2f} * x')
az.plot_hdi(x, ppc['y_pred'], hdi_prob=0.5, color='gray', smooth=False)
az.plot_hdi(x, ppc['y_pred'], color='gray', smooth=False)
plt.xlabel('x')
plt.ylabel('y', rotation=0)

st_dev3 = stats.stdev(z)
with pm.Model() as model_g:
    alfa = pm.Normal('alfa', mu=0, sd=10 * st_dev3)
    beta = pm.Normal('beta', mu=0, sd=1*st_dev3/st_dev2)
    epsilon = pm.HalfCauchy('epsilon', 5)
    miu = pm.Deterministic('miu', alfa + beta * x)
    y_pred = pm.Normal('y_pred', mu=miu, sd=epsilon, observed=y)

idata_g = pm.sample(400, tune=400, return_inferencedata=True)
az.plot_trace(idata_g, var_names=["α", "β", "ε"])
