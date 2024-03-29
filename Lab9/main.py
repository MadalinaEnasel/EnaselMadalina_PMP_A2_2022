import pymc3 as pm
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import arviz as az
import theano

theano.config.blas__ldflags = ''
# ex 1
az.style.use('arviz-darkgrid')

dummy_data = np.loadtxt('date.csv')
x_1 = dummy_data[:, 0]
y_1 = dummy_data[:, 1]
order = 5
x_1p = np.vstack([x_1 ** i for i
                  in range(1, order + 1)])
x_1s = (x_1p - x_1p.mean(axis=1, keepdims=True)) / x_1p.std(axis=1, keepdims=True)
y_1s = (y_1 - y_1.mean()) / y_1.std()
plt.scatter(x_1s[0], y_1s)
plt.xlabel('x')
plt.ylabel('y')

with pm.Model() as model_l:
    al = pm.Normal('α', mu=0, sd=1)
    be = pm.Normal('β', mu=0, sd=10)
    ep = pm.HalfNormal('ε', 5)
    mi = al + be * x_1s[0]
    y_pred = pm.Normal('y_pred', mu=mi, sd=ep, observed=y_1s)
    idata_l = pm.sample(2000, return_inferencedata=True)

with pm.Model() as model_p:
    a = pm.Normal('α', mu=0, sd=1)
    b = pm.Normal('β', mu=0, sd=10, shape=order)
    # b = pm.Normal('β', mu=0, sd=100, shape=order)
    # b = pm.Normal('β', mu=0, sd=np.array([10, 0.1, 0.1, 0.1, 0.1]), shape=order)
    e = pm.HalfNormal('ε', 5)
    m = a + pm.math.dot(b, x_1s)
    y_pred = pm.Normal('y_pred', mu=m, sd=e, observed=y_1s)
    idata_p = pm.sample(2000, return_inferencedata=True)

a_p_post = idata_p.posterior['α'].mean(("chain", "draw")).values
b_p_post = idata_p.posterior['β'].mean(("chain", "draw")).values
idx = np.argsort(x_1s[0])
y_p_post = a_p_post + np.dot(b_p_post, x_1s)
plt.plot(x_1s[0][idx], y_p_post[idx], 'C2', label=f'model order {order}')

x_new = np.linspace(x_1s[0].min(), x_1s[0].max(), 100)
α_l_post = idata_l.posterior['α'].mean(("chain", "draw")).values
β_l_post = idata_l.posterior['β'].mean(("chain", "draw")).values
y_l_post = α_l_post + β_l_post * x_new
plt.plot(x_new, y_l_post, 'C1', label='linear model')

plt.scatter(x_1s[0], y_1s, c='C0', marker='.')
plt.legend()

plt.show()
