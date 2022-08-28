"""
Instrucciones 

El comando print() , el cual es una de las directivas más sencillas de Python, simplemente imprime una línea de texto en la pantalla.

En tu primer laboratorio:

Utiliza la función print() para imprimir la linea "¡Hola, Mundo!" en la pantalla.
Una vez hecho esto, utiliza la función print() nuevamente, pero esta vez imprime tu nombre.
Elimina las comillas dobles y ejecuta el código. Observa la reacción de Python. ¿Qué tipo de error se produce?
Luego, elimina los paréntesis, vuelve a poner las comillas dobles y vuelve a ejecutar el código. ¿Qué tipo de error se produce esta vez?
Experimenta tanto como puedas. Cambia las comillas dobles a comillas simples, utiliza múltiples funciones print() en la misma línea y luego en líneas diferentes. Observa que es lo que ocurre.
"""

print("¡Hola, Mundo!")

print("JorgeHdz")

#Error generado a proposito
# print(Jorge)   #Quitar el comentario al inicio de la linea para verificar el error
#NameError: name 'Jorge' is not defined


# print"Jorge" #Quitar el comentario al inicio de la linea para verificar el error
# SyntaxError: invalid syntax

print('Jorge')

print('Jorge'),print("Otra cadena")