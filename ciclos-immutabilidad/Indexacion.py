#!/usr/bin/python3

mi_tupla = (1, 2, 3, 4, 'a', 'b', 'c', 'd')
length = len(mi_tupla)
first = 0
last = length-1
leap = 0
while length > 0:
    if leap == 0:
        print(mi_tupla[first], end="")
        first += 1
        leap = 1
    elif leap == 1:
        print(mi_tupla[last], end="")
        last -= 1
        leap = 0
    length -= 1
