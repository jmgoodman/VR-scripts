import numpy as np

import pickle

# %%
with open('viabilitylist.pickle', 'rb') as handle:
    b = pickle.load(handle)

# %%
print(b)