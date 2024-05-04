# matematicas/tools/utilez.py

import numpy as np

def check1(f, inter):
    """
    Check of f is a object type function and inter have len two
    """
    test1 = True if callable(f) and len(inter)==2 else False
    return test1

def errorDic(met):
    """
    Error options
    """
    metodos = {'abs': lambda pn1, pn: abs(pn1-pn), 
               'rel': lambda pn1, pn: abs(pn1-pn)/abs(pn),
               'relMax': lambda pn1, pn: abs(pn1-pn)/abs(max([pn, pn1])),
               'dist': lambda a, b: (b-a)/2
               }
    return metodos[met]

def SigInt(f, inter):
    """
    Return the sign of the f(a)*f(b). In the case that this product is zero, return 0.
    """
    a, b = min(inter), max(inter)
    ya, yb = f(a), f(b)
    
    if (ya*yb<0):
        sig = -1 
    elif (ya*yb>0):
        sig = 1 
    else:
        sig = 0
    return sig

def Findinterv(f, inter, Ndiv=100):
    """
    encuentra intervalos con raices
    """
    a, b = min(inter), max(inter)
    
    if (a>0) and (b>0) and abs(b-a<1):
        interDisc = np.logspace(np.log10(a), np.log10(b), Ndiv)
    else:    
        interDisc = np.linspace(a, b, Ndiv)       
               
    interFinal = []
    for i in range(1, Ndiv):
        inter2 = [interDisc[i-1], interDisc[i]]
        if (SigInt(f, inter2) < 0):
            interFinal.append(inter2)      
    return interFinal
