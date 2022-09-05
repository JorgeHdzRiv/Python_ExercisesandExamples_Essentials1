"""
Escenario
Los Beatles fueron uno de los grupos de música más populares de la década de 1960 y la banda más vendida en la historia. Algunas personas los consideran el acto más influyente de la era del rock. De hecho, se incluyeron en la compilación de la revista Time de las 100 personas más influyentes del siglo XX.

a banda sufrió muchos cambios de formación, que culminaron en 1962 con la formación de John Lennon, Paul McCartney, George Harrison y Richard Starkey (mejor conocido como Ringo Starr).


Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

Paso 1: Crea una lista vacía llamada beatles.
Paso 2: Emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison.
Paso 3: Emplea el buclefor y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: 
Stu Sutcliffe, y Pete Best.
Paso 4: Usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista.
Paso 5: Usa el método insert() para agregar a Ringo Starr al principio de la lista.
"""
# paso 1
beatles = []
print("Paso 1:", beatles)


# paso 2
beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')
print("Paso 2:", beatles)

# paso 3
n = int(input("Miembros a agregar: "))
for i in range(n):
    integrante = input("Nombre del integrante: ")
    beatles.append(integrante)
print("Paso 3:", beatles)

# paso 4
del beatles[-1]
del beatles[-1]
print("Paso 4:", beatles)

# paso 5
beatles.insert(0,'Ringo Starr ')
print("Paso 5:", beatles)


# probando la longitud de la lista
print("Los Fav", len(beatles))
