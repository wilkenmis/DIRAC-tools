###### Wilken M.
###### PhLAM
###### Université de Lille, France.
###### July, 2022.

'''

Program to obtain oscillator strengths from DR-TD calculations on DIRAC.

'''

import re
import matplotlib.pyplot as plt
import numpy as np

eV = 27.2113862127
c = 137.036

def oscillator_strengths(data,sum,osc_str):
    
    sum = np.zeros(len(data.im_polarizability[str(data.components[0])]))
    
    for i in range(len(data.components)):

        sum += abs(data.im_polarizability[str(data.components[i])])
    
        average = sum/len(data.components)

        osc_str.append(data.frequency_au[0]*average*((2.0/np.pi)/eV))

class extract_and_locate:
    
    def __init__(self):
        
        self.components = []
        self.frequency_au = [] ; self.frequency_eV = []
        self.re_polarizability = {} ; self.im_polarizability = {}
        
    def extract_keys(self,file):
        
        with open(file,'r') as infile:
            
            for line in infile:
                
                if re.search(r'<<A\( [0-9]+\),B\( [0-9]+\)>> - linear response function \(complex\):',line):
                    
                    component = '<<A( %d),B( %d)>>'%(int(line.split()[1][0]),int(line.split()[2][0]))
                    
                    if component not in self.im_polarizability:
                        
                        self.re_polarizability[component] = []; self.im_polarizability[component] = []
                    
            for key in self.im_polarizability.keys():
                
                self.components.append(key)
                
    def extract_re_im(self,file):
    		
        with open(file,'r') as infile:
            
            re_polarizability = []
            im_polarizability = []
            frequency_au = []
                
            for line in infile:	
	
                if len(line.split()) == 8 and "(converged)" in line:
                        
                    re_polarizability.append(float(line.split()[2]))
                    im_polarizability.append(float(line.split()[4]))
                    frequency_au.append(float(line.split()[0]))
            
            self.frequency_au.append(np.unique(frequency_au))
            self.frequency_eV.append(np.unique(frequency_au)*eV)
            
            re_polarizability = np.array_split(re_polarizability, len(self.components))
            im_polarizability = np.array_split(im_polarizability, len(self.components))
            
            for i in range(len(self.components)):
                
                self.re_polarizability[self.components[i]] = re_polarizability[i]
                self.im_polarizability[self.components[i]] = im_polarizability[i]

def multiple_extract(path, multiple_files, data,title):
    
    plt.figure(figsize=(10,4), dpi= 80)
    
    for file in sorted(multiple_files):
        
        file = path+file
        lab = ""
        
        if file[-12] == "_":
            lab = "%s"%(file[-11])
        else:
            lab = "%s%s"%(file[-12],file[-11])
        
        out_data = extract_and_locate()

        try:

            out_data.extract_keys(file)
            out_data.extract_re_im(file)
            data["%s"%(file)] = out_data

            for i in range(len(data[file].components)):
                #First we plot the contribution from x,y-components
                if data[file].components[i] == '<<A( 1),B( 1)>>':
                    ax = plt.subplot(121)
                    plt.plot(data[file].frequency_eV[0],2*abs(data[file].im_polarizability[data[file].components[i]]),label="%s"%(lab)) #note the 2 factor
                    plt.ylabel('|$α_{xx+yy}^{Im}$(ω)| $[a.u]$ ')
                    plt.xlabel('$\omega$ $[eV]$')
                    plt.suptitle('%s'%(title))

                #z-component
                if data[file].components[i] == '<<A( 3),B( 3)>>':
                    ax = plt.subplot(122)
                    plt.plot(data[file].frequency_eV[0],abs(data[file].im_polarizability[data[file].components[i]]),label="%s"%(lab))
                    plt.ylabel('|$α_{zz}^{Im}$(ω)| $[a.u]$ ')
                    plt.xlabel('$\omega$ $[eV]$')

        except:
            
            print('Error in file %s'%(file))


#    plt.legend(bbox_to_anchor =(1.3, 1),fontsize=9)
    plt.tight_layout()

class final_data:
    
    def __init__(self):
    
        self.freq_au = []; self.freq_eV = []; self.x = []; self.y = []; self.z = []

        self.sum = []; self.osc_str = []
        

    def obtain_list(self,multiple_files,data,path):

        freq_au_raw = [] ; freq_eV_raw = [] ; x_raw = []; y_raw = []; z_raw = []

        for file in sorted(multiple_files):
            for j in range(len(data[str(path)+str(file)].frequency_eV[0])):
                freq_au_raw.append(data[path+file].frequency_au[0][j])
                freq_eV_raw.append(data[path+file].frequency_eV[0][j])

        for file in sorted(multiple_files):
            for j in range(len(data[path+file].im_polarizability[data[path+file].components[0]])):
                x_raw.append(data[path+file].im_polarizability['<<A( 1),B( 1)>>'][j])
                y_raw.append(data[path+file].im_polarizability['<<A( 2),B( 2)>>'][j])
                z_raw.append(data[path+file].im_polarizability['<<A( 3),B( 3)>>'][j])

        freq_au = [] ; freq_eV = [] ; x = []; y = []; z = []; sum = [] ; osc_str = []

        freq_au, freq_eV = zip(*sorted(zip(freq_au_raw,freq_eV_raw),key=lambda freq_eV: freq_eV[0]))
        freq_eV, x = zip(*sorted(zip(freq_eV_raw,x_raw),key=lambda x_raw: x_raw[0])) # we use sort to avoid matplotlib conecting wrong values
        freq_eV, y = zip(*sorted(zip(freq_eV_raw,y_raw),key=lambda y_raw: y_raw[0]))
        freq_eV, z = zip(*sorted(zip(freq_eV_raw,z_raw),key=lambda z_raw: z_raw[0]))

        self.freq_au = freq_au; self.freq_eV = freq_eV; self.x = x; self.y = y; self.z = z

    def oscillator_strengths(self):

        sum = []; osc_str = []

        for i in range(len(self.freq_au)):
    
            sum.append(abs(self.x[i])+abs(self.y[i])+abs(self.z[i]))
    
            average = (abs(self.x[i])+abs(self.y[i])+abs(self.z[i]))/len(self.freq_au)

            osc_str.append(self.freq_au[i]*average*((2.0/np.pi)/eV))

        self.sum = sum ; self.osc_str = osc_str