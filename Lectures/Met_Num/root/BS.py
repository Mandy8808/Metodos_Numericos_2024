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
    interDisc = np.linspace(a, b, Ndiv)              
    interFinal = []
    for i in range(1, Ndiv):
        inter2 = [interDisc[i-1], interDisc[i]]
        if (SigInt(f, inter2) < 0):
            interFinal.append(inter2)      
    return interFinal

def Bis(f, inter, Nit, error, eps):
    a, b = min(inter), max(inter)
    
    # p0 
    p0 = (a + b)/2
    sig = SigInt(f, [a, p0]) 
    a = p0 if sig>0 else a
    b = b if sig>0 else p0
    
    # pi
    for i in range(Nit):
        pi = (a + b)/2
        epsi = errorDic(error)(a, b) if error=='dist' else errorDic(error)(pi, p0)
        if abs(epsi)<=eps or f(pi)==0:
            root = pi
            break
        
        sig = SigInt(f, [a, pi])
        a = pi if sig>0 else a
        b = b if sig>0 else pi
        
    if i==Nit-1:
        print('IMPORTANTE: la raiz encontrada no cumple el criterio de eps')
        root = pi
    return root

def roo_Bis(f, inter, Nit=1000, error='dist', eps=1e-05, Ndiv=100):
    """
    error -> 'dist', 'abs', 'rel', 'relMax'
    """
    if not check1(f, inter):
        sys.exit("Revise los parámetros dados")
    
    interF = Findinterv(f, inter, Ndiv=Ndiv)
    if len(interF)==0:
        print('No se encontraron roots en el intervalo')
        roots = None
    else:
        roots = []
        for inter in interF:
            root = Bis(f, inter, Nit, error, eps)
            roots.append(root)
            
    return roots
    