# matematicas/multiplicacion_division/multiplicacionF.py

def multiplicacion(*args):
    """
    Acá va la info
    """ 
    mult = args[0]
    for i in args[1:]:
        mult *= i  
    
    return mult