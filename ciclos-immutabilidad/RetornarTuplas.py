#!/usr/bin/python3

def obtener_coordenadas(tuple1,tuple2):
    return *tuple1, *tuple2

coordenadas = obtener_coordenadas((1, 2),(3, 4))

print(coordenadas)
