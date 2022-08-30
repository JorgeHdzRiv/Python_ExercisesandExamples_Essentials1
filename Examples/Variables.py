"""
¿Cómo almacenar los resultados intermedios, y después utilizarlos de nuevo para producir resultados subsecuentes?

Python ayudará con ello. Python ofrece "cajas" (contenedores) especiales para este propósito, estas cajas son llamadas variables - el nombre mismo sugiere que el contenido de estos contenedores puede variar en casi cualquier forma.

¿Cuáles son los componentes o elementos de una variable en Python?

Un nombre.
Un valor (el contenido del contenedor).

Si se desea nombrar una variable, se deben seguir las siguientes reglas:

* El nombre de la variable debe de estar compuesto por MAYÚSCULAS, minúsculas, dígitos, y el carácter _ (guion bajo).
* El nombre de la variable debe comenzar con una letra.
* El carácter guion bajo es considerado una letra.
* Las mayúsculas y minúsculas se tratan de forma distinta (un poco diferente que en el mundo real - Alicia y ALICIA son el mismo nombre, pero en Python son dos nombres de variable distintos, subsecuentemente, son dos variables diferentes).
* El nombre de las variables no pueden ser igual a alguna de las palabras reservadas de Python (se explicará más de esto pronto).

"""

var = 1
print(var)
#Una variable puede tener cualquier valor que desee el usuario

print("\nOtra variable")
var_2 = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var_2)

print("\nVariable mas cadena")
version = "3.9"
print("Versión de Python: " + version)

print("\nCambiando el valor de la variable")
numero = 100 #Original
numero = 200+300 #Cambio
print(numero)

#Ejemplo simple
"""
Ahora deberías de ser capaz de construir un corto programa el cual resuelva problemas matemáticos sencillos como el Teorema de Pitágoras:

El cuadrado de la hipotenusa es igual a la suma de los cuadrados de los dos catetos.

El siguiente código evalúa la longitud de la hipotenusa (es decir, el lado más largo de un triangulo rectángulo, el opuesto al ángulo recto) utilizando el Teorema de Pitágoras:
"""
print("\n***********************\n","\nTeorema de Pitagoras\n")
a = 3.0
b = 4.0
c = (a ** 2 + b ** 2) ** 0.5
print("El valor de c es: ", c)