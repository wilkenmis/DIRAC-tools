'''

Program to shift DR-TD points to match experimental data.

'''

import sys
import numpy as np
import pandas as pd   

#---------------------------------------------------------------#

## Function to load experimental data

def load_exp(file):
    data = pd.read_csv(file, sep='\t').values
    x = np.asarray(data[:,0]) ; y = np.asarray(data[:,1])
    return x,y

#---------------------------------------------------------------#

class shift:
    
    def __init__(self):
        
        self.x = []
        self.y = []
        self.max_index = 0
        self.shift = 0
        self.x_teo_shifted = []

    def find_maxima(self,PE,osc_str,esp_begin='0', esp_end='0'):
        
        self.x = np.asarray(PE); self.y = np.asarray(osc_str)
        
        if esp_begin and esp_begin == '0':
            esp_begin, esp_end = self.x[0], self.x[-1]
            self.max_index = np.where(self.y == max(self.y))[-1][-1]
            
        else:
            x_tmp = self.x[np.where(self.x < esp_begin)[-1][-1]:np.where(self.x < esp_end)[-1][-1]+1]
            y_tmp = self.y[np.where(x_tmp < esp_begin)[-1][-1]:np.where(x_tmp < esp_end)[-1][-1]+1]
            self.max_index = np.where(y_tmp == max(y_tmp))[-1][-1]

    def perform_shift(self,PE_teo, teo_max_index, PE_exp, exp_max_index):
        
        self.shift = PE_exp[exp_max_index] - PE_teo[teo_max_index]
        
        for i in range(len(PE_teo)):
            self.x_teo_shifted.append(PE_teo[i]+self.shift)

#---------------------------------------------------------------#