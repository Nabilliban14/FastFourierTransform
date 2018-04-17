import numpy as np
import scipy
from scipy import signal
import matplotlib.pyplot as plt
import math
import warnings
warnings.filterwarnings('ignore')

width = []
for i in range (1023):
    width.append(i)

n = np.linspace(0,511,512)
x = []
h = []
for i in range(len(n)):
    x.append((0.98**(n[i])*math.sin(math.pi*n[i]/24)))
    h.append((n[i]**2*(.99)**(n[i])*math.cos(math.pi*n[i]/48)))

x = np.array(x)
h = np.array(h)
c = np.convolve(x,h)

plt.plot(width, c, 'g')
markerline, stemlines, baseline = plt.stem(width, c, 'g')

plt.ylabel('Amplitude')
plt.xlabel('n value')
plt.show()
