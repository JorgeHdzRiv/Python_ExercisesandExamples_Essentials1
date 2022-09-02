"""
Escenario
La instrucción break se implementa para salir/terminar un bucle.

Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" 
como la palabra de salida secreta, en cuyo caso el mensaje "¡Has dejado el bucle con éxito". 

Debe imprimirse en la pantalla y el bucle debe terminar.

No imprimas ninguna de las palabras ingresadas por el usuario. Utiliza el concepto de ejecución condicional y la sentencia break.
"""
secret_word = "chupacabra"

word = input("Ingrese una palabra secreta: ")

while word != secret_word:
    if word == secret_word:
        break
    word = input("Ingrese una palabra nuevamente: ")
    
print("¡Has dejado el bucle con éxito")