###### Wilken M.
###### PhLAM
###### Université de Lille, France.
###### July, 2022.

'''

Here I define some of the packages I'm currently using.

'''

import os
import sys
import re
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import seaborn as sns
import warnings; warnings.filterwarnings(action='once')

large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}
plt.rcParams.update(params)
plt.style.use('seaborn-whitegrid')
sns.set_style("white")

sys.path.append("/Users/wilkenmisael/Desktop/DR_simulations/post_proc/spectra_teo_exp/src")
from broadening_functions import *
from extract_osc import *
from contributions import *
from shift_spectra import *
from cont_mul import *