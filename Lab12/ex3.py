import matplotlib.pyplot as plt
import arviz as az
import pandas as pd

centered = az.load_arviz_data("centered_eight")
non_centered = az.load_arviz_data("non_centered_eight")

centered.sample_stats.diverging.sum()
non_centered.sample_stats.diverging.sum()

_, ax = plt.subplots(1, 2, sharey=True, sharex=True, figsize=(10, 5), constrained_layout=True)

for idx, tr in enumerate([centered, non_centered]):
    az.plot_pair(tr, var_names=['mu', 'tau'], kind='scatter',
                 divergences=True, divergences_kwargs={'color':'C1'},
                 ax=ax[idx])

    ax[idx].set_title(['centered', 'non-centered'][idx])

plt.show()
