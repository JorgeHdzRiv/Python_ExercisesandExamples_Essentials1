#Crea un programa con un bucle for y una sentencia break.
# El programa debe iterar sobre los caracteres en una dirección de correo electrónico, 
# salir del bucle cuando llegue al símbolo @ e imprimir la parte antes de @ en una línea. 
# Usa el esqueleto de abajo:

"""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        # Línea de código.
    # Línea de código.

"""

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")