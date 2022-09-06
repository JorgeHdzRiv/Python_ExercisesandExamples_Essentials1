"""
La técnica que asigna cada argumento al parámetro correspondiente, es llamada paso de parámetros posicionales, 
los argumentos pasados de esta manera son llamados argumentos posicionales.

def my_function(a, b, c):
    print(a, b, c)

my_function(1, 2, 3)
"""

def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction("Skywalker", "Luke")
introduction("Quick", "Jesse")
introduction("Kent", "Clark")

"""
Python ofrece otra manera de pasar argumentos, donde el significado del argumento está definido por su nombre, 
no su posición, a esto se le denomina paso de argumentos con palabra clave.
"""
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(first_name = "James", last_name = "Bond")
introduction(last_name = "Skywalker", first_name = "Luke")


#Por supuesto que no se debe de utilizar el nombre de un parámetro que no existe.
"""
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

introduction(surname="Skywalker", first_name="Luke")
"""

#Esta ejecucion generara error

"""
Es posible combinar ambos tipos si se desea, solo hay una regla inquebrantable: se deben colocar primero los argumentos posicionales 
y después los de palabra clave.
"""
def adding(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# Invoca la función aquí.
adding(1,5,2)

"""
En ocasiones ocurre que algunos valores de ciertos argumentos son más utilizados que otros. Dichos argumentos tienen valores predefinidos 
los cuales pueden ser considerados cuando los argumentos correspondientes han sido omitidos.
"""
def introduction(first_name, last_name="González"):
    print("Hola, mi nombre es", first_name, last_name)

# Invoca la función aquí.
introduction("Juan")
