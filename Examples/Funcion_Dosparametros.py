#1 ft = 0.3048 m, y 1 in = 2.54 cm = 0.0254 m.
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

"""
Es bien conocido que 1 lb = 0.45359237 kg. Esto lo emplearemos en nuestra nueva función.

Esta función se llamará lb_to_kg:
"""
def lb_to_kg(lb):
    return lb * 0.45359237


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

print(bmi(352.5, 1.65)) #Regresara None por la condicion

#¿Cuál es el IMC de una persona que tiene 5'7" de altura y un peso de 176 lbs?
print(bmi(weight = lb_to_kg(176), height = ft_and_inch_to_m(5, 7)))

