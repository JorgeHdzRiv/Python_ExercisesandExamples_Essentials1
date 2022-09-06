"""
Un parámetro es una variable, pero existen dos factores que hacen a un parámetro diferente:

Los parámetros solo existen dentro de las funciones en donde han sido definidos, 
y el único lugar donde un parámetro puede ser definido es entre los paréntesis después del nombre de la función, 
donde se encuentra la palabra reservada def.
La asignación de un valor a un parámetro de una función se hace en el momento en que la función se manda llamar o se invoca, 
especificando el argumento correspondiente.

def function(parameter):
    ###


Recuerda que:

Los parámetros solo existen dentro de las funciones (este es su entorno natural).
Los argumentos existen fuera de las funciones, y son los que pasan los valores a los parámetros correspondientes.
Existe una clara división entre estos dos mundos.
"""

def message(number):
    print("Ingresa un número:", number)

message(3)

def message(what, number):
    print("Ingresa", what, "número", number)

message("teléfono", 11)
message("precio", 5)
message("número", "número")