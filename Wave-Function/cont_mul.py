###### Wilken M.
###### Université de Lille, France.
###### July, 2022.

'''

Script to obtain one eigenvalue informed by the user.

Note that one must take care when d instead of dd,

as it will be necessary to inform [space]d

'''




def print_eigen_mul(mulpop_input,eigenvalue,sym):
    with open(mulpop_input, "r") as infile:
        Irrep = False
        Eigenvalue = False ; Print = False
        for line in infile:
            if "Fermion ircop %s"%(sym) in line:
                Irrep = True
            if Print and line.startswith("* Electronic eigenvalue no.  %d:"%(eigenvalue+1)):
                break
            if Irrep and Eigenvalue:
                print(line)
                Print = True
            if Irrep and line.startswith("* Electronic eigenvalue no.  %d:"%(eigenvalue)):
                print(line)
                Eigenvalue = True