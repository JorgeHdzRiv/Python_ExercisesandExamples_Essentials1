"""
Objetivos
Familiarizarse con la entrada y salida de datos en Python.
Evaluar expresiones simples.

Escenario
La tarea es completar el código para evaluar y mostrar el resultado de cuatro operaciones aritméticas básicas.

El resultado debe ser mostrado en consola.

Quizá no podrás proteger el código de un usuario que intente dividir entre cero. Por ahora, no hay que preocuparse por ello.


"""

# ingresa un valor flotante para la variable a aquí
a = float(input("Valor de a: "))
# ingresa un valor flotante para la variable b aquí
b = float(input("Valor de b: "))

# muestra el resultado de la suma aquí 
print("Suma: ",a+b)
# muestra el resultado de la resta aquí
print("Resta: ",a-b)
# muestra el resultado de la multiplicación aquí
print("Multiplicacion: ",round((a*b),2))
# muestra el resultado de la división aquí
print("Division", round((a/b),2))

print("\n¡Eso es todo, amigos!")

round(2)