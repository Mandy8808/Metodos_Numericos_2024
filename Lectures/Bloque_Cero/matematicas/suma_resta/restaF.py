# matematicas/suma_resta/restaF.py

def resta(*args):
    """
    Acá va la info
    """ 
    res = args[0]
    for i in args[1:]:
        res -= i  
    
    return res