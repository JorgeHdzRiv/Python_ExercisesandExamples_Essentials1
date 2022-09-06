"""
Se necesita definirla. Aquí, la palabra definir es significativa.

Así es como se ve la definición más simple de una función:

def function_name():
    function_body


Siempre comienza con la palabra reservada def (que significa definir).
Después de def va el nombre de la función (las reglas para darle nombre a las funciones son las mismas que para las variables).
Después del nombre de la función, hay un espacio para un par de paréntesis (ahorita no contienen algo, pero eso cambiará pronto).
La línea debe de terminar con dos puntos.
La línea inmediatamente después de def marca el comienzo del cuerpo de la función - 
donde varias o (al menos una) instrucción anidada será ejecutada cada vez que la función sea invocada; 
nota: la función termina donde el anidamiento termina, se debe ser cauteloso.

"""

def message():
    print("Ingresa un valor: ")
    a = int(input())
    
print("Se comienza aquí.")
#Llamando a la funcion
message()
print("Se termina aquí.")

"""
1. Una función es un bloque de código que realiza una tarea especifica cuando la función es llamada (invocada).
Las funciones son útiles para hacer que el código sea reutilizable, que este mejor organizado y más legible. 
Las funciones contienen parámetros y pueden regresar valores.

2. Existen al menos cuatro tipos de funciones básicas en Python:

Funciones integradas las cuales son partes importantes de Python (como lo es la función print()).
Puedes ver una lista completa de las funciones integradas de Python en la siguiente liga: https://docs.python.org/3/library/functions.html.
También están las que se encuentran en módulos pre-instalados.
Funciones definidas por el usuario las cuales son escritas por los programadores para los programadores, 
puedes escribir tus propias funciones y utilizarlas libremente en tu código.
"""