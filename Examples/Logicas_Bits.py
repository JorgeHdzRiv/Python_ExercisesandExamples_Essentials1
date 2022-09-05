"""
Y aquí está la tabla de prioridades actualizada , que contiene todos los operadores presentados hasta ahora:

    Prioridad	    Operador	
1	~, +, -	        unario
2	**	
3	*, /, //, %	
4	+, -	        binario
5	<<, >>	
6	<, <=, >, >=	
7	==, !=	
8	&	
9	|	
10	=, +=, -=, *=, /=, %=, &=, ^=, |=, >>=, <<=
"""
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

#Operadores bit a bit
x = 15 #0000 1111
y = 16 #0001 0000

"""
Se utilizarán para ilustrar el significado de operadores bit a bit en Python. Analiza los ejemplos a continuación::

& hace un bit a bit and (y), por ejemplo, x & y = 0, el cual es 0000 0000 en binario.
| hace un bit a bit or (o), por ejemplo, x | y = 31, el cual es 0001 1111 en binario.
˜ hace un bit a bit not (no), por ejemplo, ˜ x = 240, el cual es 1111 0000 en binario.
^ hace un bit a bit xor, por ejemplo, x ^ y = 31, el cual es 0001 1111 en binario.
>> hace un desplazamiento bit a bit a la derecha, por ejemplo, y >> 1 = 8, el cual es 0000 1000 en binario.
<< hace un desplazamiento bit a bit a la izquierda, por ejemplo, y << 3 = , el cual es 1000 0000 en binario.
"""

x = 4
y = 1

a = x & y
b = x | y
c = ~x  # !difícil!
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)