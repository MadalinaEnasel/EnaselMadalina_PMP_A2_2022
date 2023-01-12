import matplotlib.pyplot as plt
import arviz as az
import pandas as pd

centered = az.load_arviz_data("centered_eight")
non_centered = az.load_arviz_data("non_centered_eight")

print(az.rhat(centered, var_names=["mu", "theta"]))
print(az.rhat(non_centered, var_names=["mu", "theta"]))