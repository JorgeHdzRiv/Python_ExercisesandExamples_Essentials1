"""
Existen dos convenciones adicionales en Python que no son conocidas en el mundo de las matemáticas. 
El primero nos permite utilizar un número en su representación octal.

Si un número entero esta precedido por un código 0O o 0o (cero-o), el número será tratado como un valor octal. 
Esto significa que el número debe contener dígitos en el rango del [0..7] únicamente.

0o123 es un número octal con un valor (decimal) igual a 83.

La segunda convención nos permite utilizar números en hexadecimal. Dichos números deben ser precedidos por el prefijo 0x o 0X (cero-x).

0x123 es un número hexadecimal con un valor (decimal) igual a 291. La función print() puede manejar estos valores también. Intenta esto:
"""
print("Numero octal")
print(0o123)
print("Numero hexadecimal")
print(0x123)
print("Flotantes")
print(2.5,-0.4,.4,4.)
print("Notacion cientifica")
print(3E5)
"""
La letra E (también se puede utilizar la letra minúscula e - proviene de la palabra exponente) la cual significa por diez a la n potencia.

Nota:

El exponente (el valor después de la E) debe ser un valor entero.
La base (el valor antes de la E) puede o no ser un valor entero.
"""

print("Codificando flotantes")
print(0.0000000000000000000001)

print("Cadenas")
print("Me gusta \"Monty Python\"")

print("Booleanos")
print(True, False) #True 1 and False 0

print(True > False)
print(True < False)