numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.

# Asignar un nuevo valor de 111 al primer elemento
numbers[0] = 111
print("Nuevo contenido de la lista: ", numbers)  # Contenido de la lista actual.

#copiar el valor del quinto elemento al segundo elemento.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

"""
El valor dentro de los corchetes que selecciona un elemento de la lista se llama un índice, 
mientras que la operación de seleccionar un elemento de la lista se conoce como indexación.

Nota: todos los índices utilizados hasta ahora son literales. 
Sus valores se fijan en el tiempo de ejecución, pero cualquier expresión también puede ser un índice. 
Esto abre muchas posibilidades.
"""

#Accediendo a un elemento
print(numbers[0])

#Funcion len()
"""
La longitud de una lista puede variar durante la ejecución. Se pueden agregar nuevos elementos a la lista, mientras que otros pueden eliminarse de ella. Esto significa que la lista es una entidad muy dinámica.

Si deseas verificar la longitud actual de la lista, puedes usar una función llamada len() (su nombre proviene de length - longitud).

La función toma el nombre de la lista como un argumento y devuelve el número de elementos almacenados actualmente dentro de la lista (en otras palabras, la longitud de la lista).
"""


print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

#Eliminando elementos de una lista
"""
Cualquier elemento de la lista puede ser eliminado en cualquier momento, esto se hace con una instrucción llamada del (eliminar). 
Nota: es una instrucción, no una función.

Tienes que apuntar al elemento que quieres eliminar, desaparecerá de la lista y la longitud de la lista se reducirá en uno.
"""


###

del numbers[1]  # Eliminando el segundo elemento de la lista.
print("Longitud de la nueva lista:", len(numbers))  # Imprimiendo nueva longitud de la lista.
print("\nNuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

###

"""
No puedes acceder a un elemento que no existe , 
no puedes obtener su valor ni asignarle un valor. 
"""

#Indices negativos
print(numbers[-1]) #Accede al ultimo valor de la lista