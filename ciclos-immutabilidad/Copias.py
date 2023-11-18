#!/usr/bin/python3

mi_tupla = (1, 2, 3)
copia_tupla1 = tuple(mi_tupla)  # Utilizando la función tuple()
copia_tupla2 = mi_tupla[:]  # Utilizando la segmentación
newTuple = ()

for index in range(len(mi_tupla)):
    newTuple = newTuple + (mi_tupla[index], )
print(id(copia_tupla1))
print(id(copia_tupla1))
print(id(newTuple))
