from setuptools import setup

setup(
    name = "paqMatematica",
    version = "0.1",
    description = "Esto es un ejemplo",
    author = "Armando A.",
    author_email = "arestrada@fisica.ugto.mx",
    url = "",
    install_requires = [], # añade cualquier paquete adicional que debe ser
                         # instalado una vez que se instale el paquete
    keywords = ['python', 'primer paquete'],
    packages = ['matematicas', 'matematicas.suma_resta', 'matematicas.multiplicacion_division'],  # estructura
    scripts = []
)