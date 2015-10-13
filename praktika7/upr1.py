import numpy
import matplotlib.pyplot as plt
x=numpy.arange(1,11,1)
plt.plot(x,((x**7+2*x**3-(3/(1+x**2)))/((1/(1-x))+3*7/8)))
plt.plot(x,(1/((numpy.sin(x/(x**2+2)))**2+numpy.exp(numpy.log(x)+1))))
plt.show()
