# matematicas/__init__.py

from .presentacion import hola  # notar que como es local se pone .  Para importar todas las funciones podría usar * 
from .presentacion import adios

# especificamos que modulos se importan con: from <module> import *
__all__ = ['hola']


