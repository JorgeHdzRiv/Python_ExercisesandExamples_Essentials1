"""
Python ofrece dos operadores muy poderosos, capaces de revisar la lista para verificar si un valor específico está almacenado dentro de la lista o no.

Estos operadores son:

elem in my_list
elem not in my_list


El primero de ellos (in) verifica si un elemento dado (el argumento izquierdo) está actualmente almacenado en algún lugar dentro de la lista (el argumento derecho) - el operador devuelve True en este caso.

El segundo (not in) comprueba si un elemento dado (el argumento izquierdo) está ausente en una lista - el operador devuelve True en este caso.
"""

my_list = [0, 3, 12, 8, 2]

print(5 in my_list)
print(5 not in my_list)
print(12 in my_list)

#Ejemplo de lista
my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
largest = my_list[0]

for i in my_list[1:]:
    if i > largest:
        largest = i

print(largest)

