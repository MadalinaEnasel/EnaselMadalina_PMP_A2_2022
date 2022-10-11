import numpy as np
from random import *
from scipy import stats
import arviz as az
import matplotlib.pyplot as plt

np.random.seed(1)

ss = []
sb = []
bs = []
bb = []

for i in range(100): #100 de rezultate
    ss_c = 0
    sb_c = 0
    bs_c = 0
    bb_c = 0
    for j in range(10):
        r1 = randint(1, 100)
        r2 = randint(1, 100)
        if r1<50 and r2 <30 :
            ss_c += 1
        elif r1<50 and r2>=30:
            sb_c += 1
        elif r1>=50 and r2<30:
            bs_c += 1
        else:
            bb_c += 1
    ss.append(ss_c)
    sb.append(sb_c)
    bs.append(bs_c)
    bb.append(bb_c)

az.plot_posterior({'ss':ss, 'bs':bs, 'sb':sb,'bb':bb})
plt.show()


