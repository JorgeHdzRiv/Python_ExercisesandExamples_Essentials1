"""
Escenario
Imagina una lista: no muy larga ni muy complicada, solo una lista simple que contiene algunos números enteros. 
Algunos de estos números pueden estar repetidos, y esta es la clave. No queremos ninguna repetición. Queremos que sean eliminados.

Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista. 
El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.

Nota: Asume que la lista original está ya dentro del código, no tienes que ingresarla desde el teclado. 
Por supuesto, puedes mejorar el código y agregar una parte que pueda llevar a cabo una conversación con el usuario y obtener todos los datos.

Sugerencia: Te recomendamos que crees una nueva lista como área de trabajo temporal, no necesitas actualizar la lista actual.

"""
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Escribe tu código aquí.
tmp_list = []
for num in my_list:
    if num in my_list:
        tmp_list.append(num)
        del my_list[num]
#Usando metodo burbuja para acomodar los numeros
my_list.sort()
tmp_list.sort()
#
print("La lista con elementos únicos:")
print(my_list)

print("Lista de elementos repetidos:")
print(tmp_list)

"""
Otra forma de hacer este laboratorio
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []
for number in my_list:  # Recorre todos los números de la lista original.
	if number not in new_list:  # Si el número no aparece dentro de la nueva lista...
		new_list.append(number)  # ...agregarlo aquí.
my_list = new_list[:]  # Crea una copia de new_list.
print("La lista con elementos únicos:")
print(my_list)

"""
