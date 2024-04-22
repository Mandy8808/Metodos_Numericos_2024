

def difFinNC(f, x, h, der=True, izq=False):
    """
    """
    fd = (f(x+h) - f(x))/h if der else (f(x)-f(x-h))/h 
    return fd

def difFinC(f, x, h):
    """
    """
    fd = (f(x+h/2) - f(x-h/2))/h
    return fd


def RichExt(x, f, g, h, p):
    G = (2**p*g(f,x,h/2) - g(f,x,h))/(2**p-1)
    return G