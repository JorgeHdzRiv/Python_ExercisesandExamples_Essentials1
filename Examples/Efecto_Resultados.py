"""
Todas las funciones presentadas anteriormente tienen algún tipo de efecto: producen un texto y lo envían a la consola.

Por supuesto, las funciones, al igual que las funciones matemáticas, pueden tener resultados.

Para lograr que las funciones devuelvan un valor (pero no solo para ese propósito) 
se utiliza la instrucción return (regresar o retornar).

Esta palabra nos da una idea completa de sus capacidades. 
Nota: es una palabra clave reservada de Python.


La instrucción return tiene dos variantes diferentes: considerémoslas por separado.
"""

"""
return sin una expresión
La primera consiste en la palabra reservada en sí, sin nada que la siga.

Cuando se emplea dentro de una función, provoca la terminación inmediata de la ejecución de la función,
y un retorno instantáneo (de ahí el nombre) al punto de invocación.

Nota: si una función no está destinada a producir un resultado, emplear la instrucción returnno es obligatorio, 
se ejecutará implícitamente al final de la función.

De cualquier manera, se puede emplear para terminar las actividades de una función, 
antes de que el control llegue a la última línea de la función.
"""
def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return
    
    print("¡Feliz año nuevo!")

happy_new_year()

"""
return con una expresión
La segunda variante de return está extendida con una expresión:

def function():
    return expression


Existen dos consecuencias de usarla:

Provoca la terminación inmediata de la ejecución de la función (nada nuevo en comparación con la primer variante).
Además, la función evaluará el valor de la expresión y lo devolverá (de ahí el nombre una vez más) como el resultado de la función.
"""
def boring_function():
    return 123

x = boring_function()

print("La función boring_function ha devuelto su resultado. Es:", x)

"""
No olvides:

Siempre se te permite ignorar el resultado de la función y estar satisfecho con el efecto de la función (si la función tiene alguno).
Si una función intenta devolver un resultado útil, debe contener la segunda variante de la instrucción return.
"""