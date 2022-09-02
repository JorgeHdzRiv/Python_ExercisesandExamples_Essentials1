"""
Escenario
Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. 
Están construyendo una pirámide.

Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide, es plana. 
La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, 
y generar la altura de la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas: si los constructores no tienen la cantidad suficiente de bloques 
y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.

Prueba tu código con los datos que hemos proporcionado.


Datos de Prueba

Entrada de muestra: 6

Salida esperada: La altura de la pirámide es: 3

Entrada de muestra: 20

Salida esperada: La altura de la pirámide es: 5

Entrada de muestra: 1000

Salida esperada: La altura de la pirámide es: 44

Entrada de muestra: 2

Salida esperada: La altura de la pirámide es: 1
"""
blocks = int(input("Ingresa el número de bloques: "))

#
capa = 1
height = 0
while capa <=blocks:
    height += 1
    blocks -= capa
    capa += 1
#	

print("La altura de la pirámide:", height)
