# Module
import numpy as np
import sys

def check1(f, inter):
    """
    Revisa si las entradas son correctas
    """
    test1 = True if callable(f) and len(inter)==2 else False
    return test1

def errorDic(met):
    metodos = {'abs': lambda pn1, pn: abs(pn1-pn), 
               'rel': lambda pn1, pn: abs(pn1-pn)/abs(pn),
               'relMax': lambda pn1, pn: abs(pn1-pn)/abs(max([pn, pn1])),
               'dist': lambda a, b: (b-a)/2
               }
    return metodos[met]

def SigInt(f, inter2):
    x0, x1 = inter2[0], inter2[1]
    y0, y1 = f(x0), f(x1)
    sig = -1 if y0*y1<0 else 1
    return sig

def Findinterv(f, inter, Ndiv=100):
    """
    encuentra intervalos con raices
    """
    a, b = min(inter), max(inter)
    interDisc = np.logspace(np.log10(a), np.log10(b), Ndiv) if (abs(a)<1 and a!=0) and (abs(b)<1 and b!=0)\
                else np.linspace(a, b, Ndiv)              
    interFinal = []
    for i in range(1, Ndiv):
        inter2 = [interDisc[i-1], interDisc[i]]
        if (SigInt(f, inter2) < 0):
            interFinal.append(inter2)      
    return interFinal