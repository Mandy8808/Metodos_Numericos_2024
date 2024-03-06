# Lecture Notes. Introduction to Numerical Method:
In this repository, I present a set of Jupyter notebooks (in the Spanish language) that I used in the Numerical Methods lectures   January-August 2024, DCI-UGTO.

# Folders
- Books: literature bibliograpy
- Lectures: contain the "Memo" of the course, the different lecture blocks, and a library (metodos_num) with the different numerical codes created in the course.


# TOPICS
- Bloque Cero
    - Buenas prácticas al programar.
	- Ideas básicas sobre Python y algunos paquetes fundamentales.
- Bloque Uno
    - Errores. Tipos de errores. Error Real, Absoluto y Relativo. Propagación de errores. Representación de número reales. Comparando flotantes. Suma compensada. Manipulando expresiones.
    - Root de ecuaciones de una variable. 
        - Método de bisección
        - Iteración del punto fijo
        - Método de Newton
        - Método de la secante (v1)
        - Método de la secante (v2)
    - Derivadas. 
        - Forma analítica
        - Diferencia finita
            - Aproximaciones en diferencia no centradas: Diferencia hacia adelante. Diferencia hacia atrás.
            - Aproximación de diferencia central.
            - Segunda derivada.
            - Discretización.
            - Reformulación para el caso discreto.
            - Extrapolación de Richardson
        - Diferenciación Automática 
            - Número duales
            - Funciones especiales
    - Integración numérica o cuadratura.
        - El problema a resolver.
        - Integrales de una variable.
            - Métodos tipo Newton–Cotes
                - Rectángulo
                - Punto medio
                - Trapecio
                - Simpson
        - Integraciones adaptativas
        - Integración multidimensional.
        - Comparación con `SciPy`