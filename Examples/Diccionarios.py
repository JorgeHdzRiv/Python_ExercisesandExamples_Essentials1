"""
El diccionario es otro tipo de estructura de datos de Python. 
No es una secuencia (pero puede adaptarse fácilmente a un procesamiento secuencial) y además es mutable.

Esto significa que un diccionario es un conjunto de pares de claves y valores. Nota:

Cada clave debe de ser única. No es posible tener una clave duplicada.
Una clave puede ser un tipo de dato de cualquier tipo: puede ser un número (entero o flotante), o incluso una cadena.
Un diccionario no es una lista. Una lista contiene un conjunto de valores numerados, mientras que un diccionario almacena pares de valores.
La función len() aplica también para los diccionarios, regresa la cantidad de pares (clave-valor) en el diccionario.
Un diccionario es una herramienta de un solo sentido. 
Si fuese un diccionario español-francés, podríamos buscar en español para encontrar su contraparte en francés más no viceversa.
"""

dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)

dictionary = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'león', 'caballo']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el diccionario")
        
#Metodo keys()
"""
 El método retorna o regresa una lista de todas las claves dentro del diccionario. 
 Al tener una lista de claves se puede acceder a todo el diccionario de una manera fácil y útil.
"""
print("\nMetodo keys\n")
for key in dictionary.keys():
    print(key, "->", dictionary[key])
    
#Metodo items()
"""
Este método regresa una lista de tuplas (este es el primer ejemplo en el que las tuplas son mas que un ejemplo de si mismas) 
donde cada tupla es un par de cada clave con su valor.
"""
print("\nMetodo items \n")
for spanish, french in dictionary.items():
    print(spanish, "->", french)

#Modificar
print("\nModificando el diccionario\n")
dictionary['gato'] = 'minou'
print(dictionary)

#Agregar nuevas claves
print("\nAgregar nueva clave\n")
dictionary['cisne'] = 'cygne'
print(dictionary)

#Agregando con metodo update()
print("\nAgregar nueva clave con metodo update\n")
dictionary.update({"pato": "canard"})
print(dictionary)

#Eliminando clave
print("\nEliminando clave\n")
del dictionary['perro']
print(dictionary)

#Para eliminar el ultimo elemento de la lista, se puede emplear el método popitem()
print("\nEliminando clave con metodo popitem\n")
dictionary.popitem()
print(dictionary)

