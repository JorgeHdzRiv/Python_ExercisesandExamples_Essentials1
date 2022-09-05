"""
Una rebanada es un elemento de la sintaxis de Python que permite hacer una copia nueva de una lista, o partes de una lista.

En realidad, copia el contenido de la lista, no el nombre de la lista.
"""

# Copiando la lista entera.
list_1 = [1]
list_2 = list_1[:]
list_1[0] = 2
print(list_2)

#my_list[start:end]

"""
Una rebanada de este tipo crea una nueva lista (de destino), tomando elementos de la lista de origen: 
los elementos de los índices desde el principio hasta el fin - 1.

Nota: no hasta el fin, sino hasta fin-1. Un elemento con un índice igual a fin es el primer elemento el cual no participa en la segmentación.

Es posible utilizar valores negativos tanto para el inicio como para el fin(al igual que en la indexación).
"""

# Copiando parte de la lista.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)

#La lista new_list contendrá fin - inicio (3 - 1 = 2) elementos los que tienen índices iguales a 1 y 2 (pero no 3).

"""
my_list[start:end]


Para confirmar:

start es el índice del primer elemento incluido en la rebanada.
end es el índice del primer elemento no incluido en la rebanada.
"""

#Indices negativos
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-1]
print(new_list)

#Si start especifica un elemento que se encuentra más allá del descrito por end (desde el punto de vista inicial de la lista), 
# la rebanada estará vacía:

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)

#Si omites start python dara por hecho que es el indice 0
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:3]
print(new_list)

#Del mismo modo, si omites el end en tu rebanada, se supone que deseas que el segmento termine en el elemento con el índice len(my_list).
my_list = [10, 8, 6, 4, 2]
new_list = my_list[3:]
print(new_list)

#Como hemos dicho anteriormente, el omitir el inicio y fin crea una copia de toda la lista:
my_list = [10, 8, 6, 4, 2]
new_list = my_list[:]
print(new_list)

#La instrucción del descrita anteriormente puede eliminar más de un elemento de la lista a la vez, también puede eliminar rebanadas:
my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)

#También es posible eliminar todos los elementos a la vez:
my_list = [10, 8, 6, 4, 2]
del my_list[:]
print(my_list)

#La lista quedara vacia []