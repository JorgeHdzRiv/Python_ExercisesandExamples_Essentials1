#Operaciones basicas
print("Operaciones basicas")
print(5+5)
print(6-5)
print(5*4)
print(35/7)
#El resultado producido por el operador de división siempre es flotante

#Exponentes
print("\nExponentes")
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)
"""
Recuerda: Es posible formular las siguientes reglas con base en los resultados:

Cuando ambos ** argumentos son enteros, el resultado es entero también.
Cuando al menos un ** argumento es flotante, el resultado también es flotante.
"""

#Division entera
"""
Un símbolo de // (doble diagonal) es un operador de división entera. Difiere del operador estándar / en dos detalles:

El resultado carece de la parte fraccionaria, está ausente (para los enteros), o siempre es igual a cero (para los flotantes); esto significa que los resultados siempre son redondeados.
Se ajusta a la regla entero frente a flotante.

Como se puede observar, una división de entero entre entero da un resultado entero. Todos los demás casos producen flotantes.

"""
print("\nDivision entera")
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

print(6 // 4)
print(6. // 4)
"""
Si, sería 1.5 en ambos casos. Eso está claro.

Pero, ¿Qué resultado se debería esperar con una división //?

Ejecuta el código y observa por ti mismo.


Lo que se obtiene son dos unos, uno entero y uno flotante.

El resultado de la división entera siempre se redondea al valor entero inferior mas cercano del resultado de la división no redondeada.

Esto es muy importante: el redondeo siempre va hacia abajo.
"""
print(-6 // 4)
print(6. // -4)
"""
El resultado es un par de dos negativos. El resultado real (no redondeado) es -1.5 en ambo casos. 
Sin embargo, los resultados se redondean. 
El redondeo se hace hacia el valor inferior entero, dicho valor es -2, por lo tanto los resultados son: -2 y -2.0.
"""

#Modulo
"""
El resultado de la operación es el residuo que queda de la división entera.

En otras palabras, es el valor que sobra después de dividir un valor entre otro para producir un resultado entero.

Nota: el operador en ocasiones también es denominado módulo en otros lenguajes de programación.
"""
print("\nModulo")
print(14 % 4)
"""
Como puedes observar, el resultado es dos. Esta es la razón:

14 // 4 da como resultado un 3 → esta es la parte entera, es decir el cociente.
3 * 4 da como resultado 12 → como resultado de la multiplicación entre el cociente y el divisor.
14 - 12 da como resultado 2 → este es el residuo.
"""
print(12 % 4.5)

#Notas sobre que no hacer con las divisiones
#Dividir entre cero.
#Realizar una división entera entre cero.
#Encontrar el residuo de una división entre cero.

#Enlaces
"""
El enlace de un operador determina el orden en que se computan las operaciones de los operadores con la misma prioridad, 
los cuales se encuentran dentro de una misma expresión.

La mayoría de los operadores de Python tienen un enlazado hacia la izquierda, 
lo que significa que el cálculo de la expresión es realizado de izquierda a derecha.

"""
print("\nEnlaces")
print(9 % 6 % 2)

"""
Existen dos posibles maneras de evaluar la expresión:

De izquierda a derecha: primero 9 % 6 da como resultado 3, y entonces 3 % 2 da como resultado 1.
De derecha a izquierda: primero 6 % 2 da como resultado 0, y entonces 9 % 0 causa un error fatal.
"""

print(2 ** 2 ** 3)
# 2 ** 2 → 4; 4 ** 3 → 64  enlazado izquierdo
# 2 ** 3 → 8; 2 ** 8 → 256 enlazado derecho

#El resultado muestra claramente que el operador de exponenciación utiliza enlazado del lado derecho.

#Prioridad operaciones
"""
Prioridad	        Operador	
1	+, -	        unario
2	**	
3	*, /, //, %	
4	+, -	        binario

"""
print("\nPrioridad de las operaciones")
print(2 * 3 % 5)

print("\nUso de parentesis")
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
#Desglozando la operacion
# ((5 * ((25 % 13) + 100) / (2 * 13)) // 2)   Operaciones a realizar (25 % 13)=12 y (2*13)=26
# ((5 * (12 + 100) / 26) // 2)  Operaciones a realizar (12 + 100)=112
# ((5 * 112 / 26) // 2) Operaciones a realizar (5 * 112 / 26)=5*12=560/26=21.53846153846154 
# Tomando en cuenta el enlazado izquierdo y la prioridad operaciones
# (21.53846153846154 // 2)=10.0