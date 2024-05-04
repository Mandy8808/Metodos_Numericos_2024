# Lecture Notes. Introduction to Numerical Method:
In this repository, I present a set of Jupyter notebooks (in Spanish language) that I used in the Numerical Methods lectures   January-August 2024, DCI-UGTO.

# Folders
- Books: literature bibliograpy
- Lectures: contain the "Memo" of the course, the different lecture blocks, and a library (metodos_num) with the different numerical codes created in the course.


# TOPICS
- Bloque Cero (Fueron usadas como principales referencias [Ref1](https://ellibrodepython.com), [Ref2](https://docs.python.org/3/contents.html))
    - Buenas prácticas al programar.
	- Ideas básicas sobre Python y algunos paquetes fundamentales.
- Bloque Uno (Fue usada como referencias la Bibliografía que aparece en la carpeta Books)
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
            - Número de paneles 
            - Integración Gaussiana. Posicionamiento de los nodos y peso. Generalizando el intervalo.
            - Casos Particulares. Funciones periódicas. Singularidades. Intervalos $a\to\infty$, etc.
        - Integración multidimensional.
        - Comparación con `SciPy`
    - Interpolación, splines y una segunda mirada al cálculo numérico.
        - El problema a resolver.
        - Interpolación.
            - Interpolación polinomial
                - Base monomial
                - Interpolación de Lagrange
                - Interpolación polinomial de Newton

            - Interpolación de trazados (Spline)
                - Spline Lineal (poligonales continuas)
                - Splines Cúbico clase 1
                - Splines cuadráticos
                - Splines Cúbico clase 2
            
            - Interpolación trigonométrica
                - Serie de Fourier 
                - Interpolación trigonométrica
                - Interpolación trigonométrica usando la Transformada discreta de Fourier
                    - Transformada discreta de Fourier (DFT)
                    - Transformada rápida de Fourier (FFT)
        - Comparación con `SciPy`

# Wolfram Mathematica
El curso que acá aparece se puede encontrar en: [An Elementary Introduction to the Wolfram Language](https://www.wolfram.com/language/elementary-introduction/3rd-ed/)