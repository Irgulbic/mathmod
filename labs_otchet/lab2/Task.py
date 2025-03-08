
#print((1132226527%70)+1)
#расстояние 16,7
#скорость катера в 4,5 разабольше
#{dr/dt = v  r*dq/dt=(n**2 -1)**0,5 * v
#dr/dq = r/(4,5)**2 - 1)**0,5 = r / (20,25 - 1)**0,5 = 
# = r/(19,25)**0,5 == r/4,387

#q = 0, r = 0
# r0 = 16,7

#dr/dq = r/4,387
# r = r0 * e **(q/4,387)

#r(q) = 16,7 * e **(q/4,387) - траектория катера в полярных коор
# r(q) = v * t - траектория лодки в полярных коорд

import numpy as np
import matplotlib.pyplot as plt

#Parametri
r0 = 16.7
n = 4.5
v = 1

#traektoria katera
theta = np.linspace(0, 2 * np.pi, 1000)
r = r0 * np.exp(theta / np.sqrt(n**2 -1))

#traektoria lodki
t = np.linspace(0, 10, 1000)
r_lodka = v * t

#Postroenie grafika
plt.polar(theta, r, label = 'Траекторпия катера')
plt.polar(np.linspace(0, 2 * np.pi, 1000), r_lodka, label='Траектория лодки')
plt.legend()
plt.show()

#answers
#1. uravnenie dvijenia katera : r(q) = 16,7 * e ** (q/4,387)
#2. traektoria lodki: r(q) = v * t
#3. grafik