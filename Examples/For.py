"""
La palabra reservada for abre el bucle for; 
nota - No hay condición después de eso; no tienes que pensar en las condiciones, ya que se verifican internamente, sin ninguna intervención.
Cualquier variable después de la palabra reservada for es la variable de control del bucle; cuenta los giros del bucle y lo hace automáticamente.
La palabra reservada in introduce un elemento de sintaxis que describe el rango de valores posibles que se asignan a la variable de control.
La función range() (esta es una función muy especial) es responsable de generar todos los valores deseados de la variable de control; en nuestro ejemplo, la función creará (incluso podemos decir que alimentará el bucle con) valores subsiguientes del siguiente conjunto: 0, 1, 2 .. 97, 98, 99; nota: en este caso, la función range() comienza su trabajo desde 0 y lo finaliza un paso (un número entero) antes del valor de su argumento.
Nota la palabra clave pass dentro del cuerpo del bucle - no hace nada en absoluto; es una instrucción vacía : la colocamos aquí porque la sintaxis del bucle for exige al menos una instrucción dentro del cuerpo (por cierto, if, elif, else y while expresan lo mismo).
"""

for i in range(10):
    print("El valor de i es actualmente", i)

print("\n-----------------------------------\n")  
for j in range(2, 8):
    print("El valor de j es actualmente", i)

print("\n-----------------------------------\n")  
power = 1
for expo in range(16):
    print("2 a la potencia de", expo, "es", power)
    power *= 2
    
print("\n-----------------------------------\n") 

for k in range(2, 8, 3):
    print("El valor de k es actualmente", k)

