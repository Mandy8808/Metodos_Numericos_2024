# matematicas/__init__.py

from .presentacion import hola  # notar que como es local se pone .  Para importar todas las funciones podría usar * 
from .presentacion import adios

from .multiplicacion_division import multiplicacion
from .multiplicacion_division import division

# especificamos que modulos se importan con: from <module> import *
__all__ = [
    # presentacion
    'hola', 'adios',
    # divisionF
    'division',
    # multiplicacionF
    'multiplicacion',
    #suma y resta
    'suma', 'resta'
]


