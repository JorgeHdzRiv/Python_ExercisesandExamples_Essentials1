"""
La función input() es capaz de leer datos que fueron introducidos por el usuario y pasar esos datos al programa en ejecución.

El programa entonces puede manipular los datos, haciendo que el código sea verdaderamente interactivo.
"""
print("Dime algo...")
anything = input()
print("Mmm...", anything, "...¿en serio?")

"""
*El programa solicita al usuario que inserte algún dato desde la consola (seguramente utilizando el teclado, 
aunque también es posible introducir datos utilizando la voz o alguna imagen).

*La función input() es invocada sin argumentos (es la manera mas sencilla de utilizar la función); 
la función pondrá la consola en modo de entrada; aparecerá un cursor que parpadea, y podrás introducir datos con el teclado, 
al terminar presiona la tecla Enter; todos los datos introducidos serán enviados al programa a través del resultado de la función.

*Nota: el resultado debe ser asignado a una variable; esto es crucial, si no se hace los datos introducidos se perderán.
*Después se utiliza la función print() para mostrar los datos que se obtuvieron, con algunas observaciones adicionales.

"""

# Probando mensajes de error.

#anything = input("Inserta un número: ")
#something = anything ** 2.0
#print(anything, "al cuadrado es", something)

#La última línea lo explica todo, se intentó aplicar el operador ** a 'str' (una cadena) acompañado por un 'float' (valor flotante).

#Casteo
anything = float(input("Inserta un número: "))
something = anything ** 2.0
print(anything, "al cuadrado es", something)

"""
Python ofrece dos simples funciones para especificar un tipo de dato y resolver este problema, aquí están: int() y float().

Sus nombres indican cual es su función:

La función int() toma un argumento (por ejemplo, una cadena: int(string)) e intenta convertirlo a un valor entero; 
si llegase a fallar, el programa entero fallará también (existe una manera de solucionar esto, se explicará mas adelante).

La función float() toma un argumento (por ejemplo, una cadena: float(string)) e intenta convertirlo a flotante (el resto es lo mismo).

Esto es muy simple y muy efectivo. Sin embargo, estas funciones se pueden invocar directamente pasando el resultado de la función input() directamente. No hay necesidad de emplear variables como almacenamiento intermedio.
"""
