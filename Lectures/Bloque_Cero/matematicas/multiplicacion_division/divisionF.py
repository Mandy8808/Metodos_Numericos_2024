# matematicas/multiplicacion_division/divisionF.py

def division(*args):
    """
    Acá va la info
    """
    try:
        if len(args)==2 and args[1]!=0:
            div = args[0]/args[1]
    except ValueError:
         print('Error el denominador es cero o no se proporcionó')
        
    return div