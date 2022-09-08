school_class = {}

while True:
    name = input("Ingresa el nombre del estudiante: ")
    if name == '':
        break

    score = int(input("Ingresa la calificación del estudiante (0-10): "))
    if score not in range(0, 11):
        break

    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)

for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
"""
Imaginemos el siguiente problema:

Necesitas un programa para calcular los promedios de tus alumnos.

El programa pide el nombre del alumno seguido de su calificación.

Los nombres son ingresados en cualquier orden.

El ingresar un nombre vacío finaliza el ingreso de los datos (nota 1: ingresar una puntuación vacía generará la excepción ValueError, 
pero no te preocupes por eso ahora, verás cómo manejar tales casos cuando hablemos de excepciones en el segundo parte de la serie del curso).

Una lista con todos los nombre y el promedio de cada alumno debe ser mostrada al final.

Observa el código en el editor, se muestra la solución.

Ahora se analizará línea por línea:

Línea 1: crea un diccionario vacío para ingresar los datos: el nombre del alumno es empleado como clave, mientras que todas las calificaciones asociadas son almacenadas en una tupla (la tupla puede ser el valor de un diccionario, esto no es un problema).
Línea 3: se ingresa a un bucle "infinito" (no te preocupes, saldrémos de el en el momento indicado).
Línea 4: se lee el nombre del alumno aquí.
Línea 5-6: si el nombre es una cadena vacía (), salimos del bucle.
Línea 8: se pide la calificación del estudiante (un valor entero en el rango del 1-10).
Línea 9-10: si la puntuación ingresada no está dentro del rango de 0 a 10, se abandona el bucle.
Línea 12-13: si el nombre del estudiante ya se encuentra en el diccionario, se alarga la tupla asociada con la nueva calificación (observa el operador +=).
Línea 14-15: si el estudiante es nuevo (desconocido para el diccionario), se crea una entrada nueva, su valor es una tupla de un solo elemento la cual contiene la calificación ingresada.
Línea 17: se itera a través de los nombres ordenados de los estudiantes.
Línea 18-19: inicializa los datos necesarios para calcular el promedio (sum y counter).
Línea 20-22: se itera a través de la tupla, tomado todas las calificaciones subsecuentes y actualizando la suma junto con el contador.
Línea 23: se calcula e imprime el promedio del alumno junto con su nombre.
"""

