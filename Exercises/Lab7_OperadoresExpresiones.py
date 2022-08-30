"""
Objetivos

Familiarizarse con los conceptos de números, operadores y operaciones aritméticas en Python.
Realizar cálculos básicos.


Escenario

Observa el código en el editor: lee un valor flotante, lo coloca en una variable llamada x, e imprime el valor de la variable llamada y. 
Tu tarea es completar el código para evaluar la siguiente expresión:

3x^3 - 2x^2 + 3x - 1

El resultado debe ser asignado a y.

Recuerda que la notación algebraica clásica muy seguido omite el operador de multiplicación, aquí se debe de incluir de manera explicita. Nota como se cambia el tipo de dato para asegurarnos de que x es del tipo flotante.

Mantén tu código limpio y legible, y pruébalo utilizando los datos que han sido proporcionados. No te desanimes por no lograrlo en el primer intento. Se persistente y curioso.


Datos de Prueba
Entrada de Muestra

x = 0
x = 1
x = -1

Salida Esperada

y = -1.0
y = 3.0
y = -9.0
"""
x =  float(-1) #Aqui podemos cambiar el valor de x
y = (3*x**3)-(2*x**2)+3*x-1
print("y =", y)

#Solucion avanzada
x_list = [0,1,-1]
y_list = []

for x in x_list:
    y = float((3*x**3)-(2*x**2)+3*x-1)
    y_list.append(y)

print("Los valores obtenidos son: ",y_list)