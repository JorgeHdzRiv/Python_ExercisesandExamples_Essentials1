"""
Ambos bucles while y for, tienen una característica interesante (y rara vez se usa).

Los bucles también pueden tener la rama else, como los if.

La rama else del bucle siempre se ejecuta una vez, independientemente de si el bucle ha entrado o no en su cuerpo.

"""
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else:", i)
