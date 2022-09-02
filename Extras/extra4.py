"""
Crea un programa con un bucle for y una sentenciacontinue. 
El programa debe iterar sobre una cadena de dígitos, reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla. 
Usa el esqueleto de abajo:

for digit in "0165031806510":
    if digit == "0":
        # Línea de código.
        # Línea de código.
    # Línea de código.
"""

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")