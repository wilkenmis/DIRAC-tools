###### Wilken M.
###### PhLAM
###### Université de Lille, France.
###### July, 2022.

'''

Broadening functions

'''

import numpy as np

def lorentzian(x, y, xmin, xmax, xstep, gamma):
    xi = np.arange(xmin,xmax,xstep); yi=np.zeros(len(xi))
    for i in range(len(xi)):
        for k in range(len(x)):
            yi[i] = yi[i] + y[k] * gamma / ( (xi[i]-x[k])**2 + (gamma/2.)**2 ) / np.pi
    return xi,yi

def gaussian(x, y, xmin, xmax, xstep, sigma):
    xi = np.arange(xmin,xmax,xstep); yi=np.zeros(len(xi))
    for i in range(len(xi)): 
        for k in range(len(y)):
            yi[i] = yi[i] + y[k]*np.e**(-((xi[i]-x[k])**2)/(2*sigma**2))
    return xi,yi