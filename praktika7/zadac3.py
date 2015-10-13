import numpy as np
import matplotlib.pyplot as plt
def y (x):
    return (np.log((x**2+1),1+np.tan(1/((np.sin(x))**2)))*np.exp(-np.fabs(x)/10))
x=np.arange(-3,13.1,0.1)
plt.plot(x, y (x))
plt.title(r'$log((x**2+1),1+np.tan(1/((np.sin(x))**2)))*exp(-np.fabs(x)/10)$')
plt.grid(True)
plt.show()
