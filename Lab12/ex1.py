import matplotlib.pyplot as plt
import arviz as az
import pandas as pd

centered = az.load_arviz_data("centered_eight")
non_centered = az.load_arviz_data("non_centered_eight")

# Ex1

info = az.plot_trace(centered, divergences='top', compact=False)
info = az.plot_trace(non_centered, divergences='top', compact=False)

plt.show()