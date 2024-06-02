# matematicas/root/__init__.py
"""
This is a module that contain all differentiation implementations
"""
print('Loading Differentiation modules')

from .BS import Bis, roo_Bis  
from .secv1 import secv1, roo_Secv1  
from .tools.utilez import check1, errorDic, SigInt, Findinterv

# especificamos que modulos se importan con: from <module> import *
__all__ = ['Bis', 'roo_Bis', 'check1', 'errorDic', 'SigInt', 'Findinterv',
           'secv1', 'roo_Secv1']
