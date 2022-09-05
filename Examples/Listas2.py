#Agregando elementos a una lista

#Un nuevo elemento puede ser añadido al final de la lista existente: list.append(value)

"""
Dicha operación se realiza mediante un método llamado append(). 
Toma el valor de su argumento y lo coloca al final de la lista que posee el método.

La longitud de la lista aumenta en uno.

El método insert() es un poco más inteligente: puede agregar un nuevo elemento en cualquier lugar de la lista, no solo al final.
list.insert(location, value)

Toma dos argumentos:

El primero muestra la ubicación requerida del elemento a insertar. 
Nota: todos los elementos existentes que ocupan ubicaciones a la derecha del nuevo elemento 
(incluido el que está en la posición indicada) se desplazan a la derecha, para hacer espacio para el nuevo elemento.

El segundo es el elemento a insertar.
"""

numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#Creando una lista desde cero
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)

#Suma de elementos
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)