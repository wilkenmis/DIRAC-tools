###### Wilken M.
###### PhLAM
###### Université de Lille, France.
###### July, 2022.

'''

Program to obtain contributions from DR-TD calculations on DIRAC.

You'll need to inform the file, the component, the inactive orbital.

Observe that here the smaller contribution is set to be 10%.

'''

import numpy as np   

eV = 27.2113862127

#---------------------------------------------------------------#

class analysis:
    
    def __init__(self):
        self.analysis_data = {'XDIPLEN':[[],[],[],[],[]],'YDIPLEN':[[],[],[],[],[]],'ZDIPLEN':[[],[],[],[],[]]}

    def copying_analysis(self, file, vir_orb):

        with open(file,'r') as infile:

            for line in infile:

                if "** E solution vectors :" in line:
                    #set the component
                    component = (line.split()[5])
                
                if "Freq.:" and "Norm:" and "Residual norm:" in line:
                    #take freq
                    freq = float(line.split()[1])

                if len(line.split()) == 4 and line.split()[1] == '--->':

                    if "NaN%" in line:
                        print('Problem with file %s'%(file))

                    if int(line.split()[0][:-7]) == int(vir_orb) and float(line.split()[3][:-1]) > 10:
                        self.analysis_data[component][0].append(freq)
                        self.analysis_data[component][1].append(freq*eV)
                        self.analysis_data[component][2].append(float(line.split()[0][:-7]))
                        self.analysis_data[component][3].append(float(line.split()[2][:-7]))
                        self.analysis_data[component][4].append(float(line.split()[3][:-1]))

#---------------------------------------------------------------#

class multi_analysis:
    
    def __init__(self):
        self.analysis_data = {'XDIPLEN':[[],[],[],[],[]],'YDIPLEN':[[],[],[],[],[]],'ZDIPLEN':[[],[],[],[],[]]}

    def copying_analysis(self, path, list_files, in_orb):
        
        for i in range(len(list_files)):

            with open(path+list_files[i],'r') as infile:

                for line in infile:

                    if "** E solution vectors :" in line:
                        #set the component
                        component = (line.split()[5])
                    
                    if "Freq.:" and "Norm:" and "Residual norm:" in line:
                        #take freq
                        freq = float(line.split()[1])

                    if len(line.split()) == 4 and line.split()[1] == '--->':
                        if int(line.split()[0][:-7]) == int(in_orb) and float(line.split()[3][:-1]) > 10:
                            self.analysis_data[component][0].append(freq)
                            self.analysis_data[component][1].append(freq*eV)
                            self.analysis_data[component][2].append(float(line.split()[0][:-7]))
                            self.analysis_data[component][3].append(float(line.split()[2][:-7]))
                            self.analysis_data[component][4].append(float(line.split()[3][:-1]))

#---------------------------------------------------------------#

class multi_analysis_vir:
    
    def __init__(self):
        self.analysis_data = {'XDIPLEN':[[],[],[],[],[]],'YDIPLEN':[[],[],[],[],[]],'ZDIPLEN':[[],[],[],[],[]]}

    def copying_analysis(self, path, list_files, in_orb, vir_orb):
        
        for i in range(len(list_files)):

            with open(path+list_files[i],'r') as infile:

                for line in infile:

                    if "** E solution vectors :" in line:
                        #set the component
                        component = (line.split()[5])
                    
                    if "Freq.:" and "Norm:" and "Residual norm:" in line:
                        #take freq
                        freq = float(line.split()[1])

                    if len(line.split()) == 4 and line.split()[1] == '--->':
                        if int(line.split()[0][:-7]) == int(in_orb) and int(line.split()[2][:-7]) == int(vir_orb) and float(line.split()[3][:-1]) > 10:
                            self.analysis_data[component][0].append(freq)
                            self.analysis_data[component][1].append(freq*eV)
                            self.analysis_data[component][2].append(float(line.split()[0][:-7]))
                            self.analysis_data[component][3].append(float(line.split()[2][:-7]))
                            self.analysis_data[component][4].append(float(line.split()[3][:-1]))