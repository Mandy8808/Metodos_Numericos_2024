# Module
from .tools.utilez import check1, errorDic, SigInt, Findinterv
import sys

def Bis(f, inter, Nit, error, eps):
    """
    The Bisection method
    In:
    f: it is a lambda or def object that represent a function f(x).
    inter: it is the interval [a, b] where we will find the roots.
    Nit: number of iterations. By default it is 1000.
    error: type of error used. The possibilities are {'dist', 'abs', 'rel', 'relMax'}. By default, it is 'dist'.
    eps: error bound, by default it is 1e-05.
    
    Out:
    roots: the found root
    """
    a, b = min(inter), max(inter)
    
    # p0 
    p0 = (a + b)/2
    sig = SigInt(f, [a, p0]) 
    if (sig>0):
        a = p0
    else:
        b = p0

    # pi
    for i in range(Nit):
        pi = (a + b)/2
        sig = SigInt(f, [a, pi])
        
        epsi = errorDic(error)(a, b) if error=='dist' else errorDic(error)(pi, p0)
        if abs(epsi)<=eps or sig==0.:
            root = pi
            break
        
        if (sig>0):
            a, p0 = pi, pi
        else:
            b, p0 = pi, pi
        
    if i==Nit-1:
        print('IMPORTANTE: la raiz encontrada no cumple el criterio de eps')
        root = pi
    return root

def roo_Bis(f, inter, Nit=1000, error='dist', eps=1e-05, Ndiv=100):
    """
    In:
    f: it is a lambda or def object that represent a function f(x).
    inter: it is the interval [a, b] where we will find the roots.
    Nit: number of iterations. By default it is 1000.
    error: type of error used. The possibilities are {'dist', 'abs', 'rel', 'relMax'}. By default, it is 'dist'.
    eps: error bound, by default it is 1e-05.
    Ndiv: number of subdivisions that the interval [a, b] will be divided, by default 100 is used.
    
    Out:
    roots: a list with the found roots
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
    