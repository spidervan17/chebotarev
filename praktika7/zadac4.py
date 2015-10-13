import math
import pylab
from matplotlib import mlab

tmin = -20.0
tmax = 20.0

dt = 0.01
tlist = mlab.frange (tmin, tmax, dt)

pylab.ion()

for a in range (100):
        xlist = [math.sin (4*t + a/2.6) for t in tlist]
        ylist = [math.cos (7*t) for t in tlist]
        pylab.clf()
        pylab.plot (xlist, ylist)
        pylab.draw()

pylab.close()
