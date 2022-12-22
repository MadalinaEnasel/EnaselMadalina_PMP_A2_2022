import numpy as np
import arviz as az
import matplotlib.pyplot as plt
import scipy.stats as stats
import statistics

#Exercitiul 2

N = 10000
error_med = 0
err_list = []
for i in range(0,4):
    x, y = np.random.uniform(-1, 1, size=(2, N))
    inside = (x**2 + y**2) <= 1
    pi = inside.sum()*4/N
    error = abs((pi - np.pi) / pi) * 100
    error_med += error
    err_list.append(error)
error_med = error_med/2
outside = np.invert(inside)
plt.figure(figsize=(8, 8))
plt.plot(x[inside], y[inside], 'b.')
plt.plot(x[outside], y[outside], 'r.')
plt.plot(0, 0, label=f'π*= {pi:4.3f}\nerror = {error:4.3f}', alpha=0)
plt.axis('square')
plt.xticks([])
plt.yticks([])
plt.legend(loc=1, frameon=True, framealpha=0.9)
plt.show()
plt.errorbar(x,y,error_med)
plt.show()

print("Standard Deviation of Error is % s ", (statistics.stdev(err_list)))
print("Mean of Error is % s ", (statistics.mean(err_list)))

print("cu cat N e mai mare, cu atat numarul e mai aproape de adevaratul pi => eroarea e mai mica")