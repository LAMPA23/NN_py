import numpy as np

M = (np.random.rand(5)*20).astype(int)
a = np.argmin(M)
print(M)
print(a)