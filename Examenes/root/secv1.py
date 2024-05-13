# Module
from .BS import Bis
from .tools.utilez import check1, errorDic, Findinterv
import sys

def secv1(f, approx, Nit, error, eps):
    """
    The Bisection method
    In:
    f: it is a lambda or def object that represent a function f(x).
    approx: it is the approximations [p0, p1].
    Nit: number of iterations. By default it is 1000.
    error: type of error used. The possibilities are {'dist', 'abs', 'rel', 'relMax'}. By default, it is 'dist'.
    eps: error bound, by default it is 1e-05.
    
    Out:
    roots: the found root
    """
    p0, p1 = approx
    q0, q1 = f(p0), f(p1)
    
    for i in range(Nit):
        pi = p1-q1*(p1-p0)/(q1-q0)
        
        epsi = errorDic(error)(pi, p1) if error=='dist' else errorDic(error)(pi, p1)
        if abs(epsi)<=eps:
            root = pi
            break
        
        # update
        p0, q0 = p1, q1
        p1, q1 = pi, f(pi)
        
    if i==Nit-1:
        print('IMPORTANTE: la raiz encontrada no cumple el criterio de eps')
        root = pi
    return root

def roo_Secv1(f, inter, delt=2., Nit=1000, error='dist', eps=1e-05, Ndiv=100):
    """
    In:
    f: it is a lambda or def object that represent a function f(x).
    inter: it is the interval [a, b] where we will find the roots.
    delt: it is the value that is added to p0.
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
            # first Bis
            p0 = Bis(f, inter, Nit, error, eps)
            p1 = p0 + delt
            root = secv1(f, [p0, p1], Nit, error, eps)
            roots.append(root)         
    return roots
    