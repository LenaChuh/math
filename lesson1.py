%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10)
for k in [1,3,6]:
    plt.figure(figsize=(110,50))
    plt.plot(x, np.cos(k*x))
    print(x)
