import numpy as np
import arviz as az
import pymc3 as pm

# ex 1

clusters = 3
n_cluster = [160, 170, 170]
n_total = sum(n_cluster)
means = [5, 0, 2.5]
std_devs = [2, 2, 2]
mix = np.random.normal(np.random.normal(np.repeat(means, n_cluster), np.repeat(std_devs, n_cluster)),
                       np.repeat(means, n_cluster))
az.plot_kde(np.array(mix))

# ex 2

clusters = [2, 3, 4]
models = []
idatas = []
for cluster in clusters:
    with pm.Model() as model:
        p = pm.Dirichlet('p', a=np.ones(cluster))
        means = pm.Normal('means',
                          mu=np.linspace(cs_exp.min(), cs_exp.max(), cluster),
                          sd=10, shape=cluster,
                          transform=pm.distributions.transforms.ordered)
        sd = pm.HalfNormal('sd', sd=10)
        y = pm.NormalMixture('y', w=p, mu=means, sd=sd, observed=cs_exp)
        idata = pm.sample(1000, tune=2000, target_accept=0.9, random_seed=123, return_inferencedata=True)
        idatas.append(idata)
        models.append(model)

# ex 3

comp_waic = az.compare(dict(zip([str(c) for c in clusters], idatas)),
                       method='BB-pseudo-BMA', ic="waic", scale="deviance")


az.compare_plot(comp_waic)
comp_loo = az.compare(dict(zip([str(c) for c in clusters], idatas)),
                      method='BB-pseudo-BMA', ic="loo", scale="deviance")
az.compare_plot(comp_loo)
