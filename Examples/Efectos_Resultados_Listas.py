def list_sum(lst):
    s = 0
    
    for elem in lst:
        s += elem
    
    return s

print(list_sum([5, 4, 3]))

#Error tipico
# print(list_sum(5))

#Esto se debe al hecho de que el bucle for no puede iterar un solo valor entero.

#Resultado en lista
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list

print(strange_list_fun(5))