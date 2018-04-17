import numpy as np
import scipy
from scipy import signal
import matplotlib.pyplot as plt
import math
import warnings
warnings.filterwarnings('ignore')

width = []
for i in range (1000):
    width.append(i)

n = np.linspace(1,1001,1000)
n_dir = []
n_fast = []
for i in range(len(n)):
    n_dir.append(2*n[i]**2)
    n_fast.append(12*n[i]*math.log(2*n[i],2) + 8*n[i] + 4)

n_dir = np.array(n_dir)
n_fast = np.array(n_fast)

plt.plot(width, n_dir, 'g')
markerline, stemlines, baseline = plt.stem(width, n_dir, 'g')

plt.plot(width, n_fast, 'b')
markerline, stemlines, baseline = plt.stem(width, n_fast, 'b')

plt.ylabel('Number of Instructions')
plt.xlabel('L value')
plt.title('n_dir is green, n_fast is blue')
plt.show()
