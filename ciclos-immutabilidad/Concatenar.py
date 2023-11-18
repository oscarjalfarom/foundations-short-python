#!/usr/bin/python3

def tuplaMul(tupla1,tupla2,escalar):
    return escalar*tupla1+escalar*tupla2

coordenadas = tuplaMul((1,2),(4,5),3)

print(coordenadas)
