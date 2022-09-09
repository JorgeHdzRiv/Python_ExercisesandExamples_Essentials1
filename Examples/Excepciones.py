"""
Puedes ver dos bloques aquí:

El primero, comienza con la palabra clave reservada try: este es el lugar donde se coloca el código que se sospecha que es riesgoso 
y puede terminar en caso de un error; nota: este tipo de error lleva por nombre excepción, 
mientras que la ocurrencia de la excepción se le denomina generar; podemos decir que se genera (o se generó) una excepción.


El segundo, la parte del código que comienza con la palabra clave reservada except: esta parte fue diseñada para manejar la excepción; 
depende de ti lo que quieras hacer aquí: puedes limpiar el desorden o simplemente puede barrer el problema debajo de la alfombra 
(aunque se prefiere la primera solución).

Entonces, podríamos decir que estos dos bloques funcionan así:

La palabra clave reservada try marca el lugar donde intentas hacer algo sin permiso.
La palabra clave reservada except comienza un lugar donde puedes mostrar tu talento para disculparte o pedir perdón.

try:
	# Es un lugar donde
	# tu puedes hacer algo 
    # sin pedir permiso.
except:
	# Es un espacio dedicado 
    # exclusivamente para pedir perdón.

"""

try:
    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))        
except:
    print('No se que hacer con', value)
"""
Cualquier fragmento de código colocado entre try y except se ejecuta de una manera muy especial: 
cualquier error que ocurra aquí dentro no terminará la ejecución del programa. 

En cambio, el control saltará inmediatamente a la primera línea situada después de la palabra clave reservada except, 
y no se ejecutará ninguna otra línea del bloque try.

El código en el bloque except se activa solo cuando se ha encontrado una excepción dentro del bloque try. 

No hay forma de llegar por ningún otro medio.

Cuando el bloque try o except se ejecutan con éxito, el control vuelve al proceso normal de ejecución y 
cualquier código ubicado más allá en el archivo fuente se ejecuta como si no hubiera pasado nada.
"""

try:
    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')  

#Excepcion por defecto
try:
    value = input('Ingresa un número natural: ')
    print('El recíproco de', value, 'es', 1/int(value))        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.')    
except:
    print('Ha sucedido algo extraño, ¡lo siento!')