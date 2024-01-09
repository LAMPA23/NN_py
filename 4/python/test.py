import numpy as np

a = np.random.rand(5,5) * 10 
a = a.astype(int)

for i,e in np.ndenumerate(a):
    print(f'{i}')
