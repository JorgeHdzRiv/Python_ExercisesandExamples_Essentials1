"""
Objetivos

Familiarizarse con el concepto de variables y trabajar con ellas.
Realizar operaciones básicas y conversiones.
Experimentar con el código de Python.

Escenario

Millas y kilómetros son unidades de longitud o distancia.

Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, complementa el programa en el editor para que convierta de:

Millas a kilómetros.
Kilómetros a millas.
No se debe cambiar el código existente. Escribe tu código en los lugares indicados con ###. 
Prueba tu programa con los datos que han sido provistos en el código fuente.


Pon mucha atención a lo que esta ocurriendo dentro de la función print(). 
Analiza como es que se proveen múltiples argumentos para la función, y como es que se muestra el resultado.

Nota que algunos de los argumentos dentro de la función print() son cadenas (por ejemplo "millas son", y otros son variables (por ejemplo miles).

TIP

Hay una cosa interesante más que esta ocurriendo. 
¿Puedes ver otra función dentro de la función print()? Es la función round(). 
Su trabajo es redondear la salida del resultado al número de decimales especificados en el paréntesis, y regresar un valor flotante (dentro de la función round() se puede encontrar el nombre de la variable, el nombre, una coma, y el número de decimales que se desean mostrar). Se hablará más de esta función muy pronto, no te preocupes si no todo queda muy claro. Solo se quiere impulsar tu curiosidad.


Resultado Esperado
7.38 millas son 11.88 kilómetros
12.25 kilómetros son 7.61 millas

"""
#Solucion
kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")