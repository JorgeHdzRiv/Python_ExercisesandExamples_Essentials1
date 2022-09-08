"""
Lo primero que distingue una lista de una tupla es la sintaxis empleada para crearlas.
Las tuplas utilizan paréntesis, mientras que las listas usan corchetes, 
aunque también es posible crear una tupla tan solo separando los valores por comas.
"""

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125

print(tuple_1)
print(tuple_2)

empty_tuple = ()

#Si deseas leer los elementos de una tupla, lo puedes hacer de la misma manera que se hace con las listas.
my_tuple = (1, 10, 100, 1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)
    
"""
La función len() acepta tuplas, y regresa el número de elementos contenidos dentro.
El operador + puede unir tuplas (ya se ha mostrado esto antes).
El operador * puede multiplicar las tuplas, así como las listas.
Los operadores in y not in funcionan de la misma manera que en las listas.
"""

my_tuple = (1, 10, 100)

t1 = my_tuple + (1000, 10000)
t2 = my_tuple * 3

print(len(t2))
print(t1)
print(t2)
print(10 in my_tuple)
print(-10 not in my_tuple)