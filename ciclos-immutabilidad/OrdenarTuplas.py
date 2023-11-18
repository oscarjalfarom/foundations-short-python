#!/usr/bin/python3

def ordTuple(tuple1):
    temp = ()
    for index in range(len(tuple1)-1):
        flag = 0
        for ver in range(len(temp)):
            if tuple1[index] == temp[ver]:
                flag = 1
                break
        if flag != 1:
            temp = temp + (tuple1[index], )
    temp = sorted(temp)
    return temp


mi_tupla = (1, 2, 3, 4, 5, 3, 4)
tupla_invertida = mi_tupla[::-1]  # Invertir
tupla_ordenada = tuple(sorted(mi_tupla))  # Ordenar
print(mi_tupla)
print(tupla_invertida)
print(tupla_ordenada)

newTuple = ordTuple(tupla_invertida)
