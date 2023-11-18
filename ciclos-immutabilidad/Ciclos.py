#!/usr/bin/python3

from typing import Tuple, TypeAlias

Frutas: TypeAlias = "Tuple[str]"

frutas:Frutas = ('manzana', 'banana', 'cereza')
fruit:str

for fruit in frutas:
  if fruit != "manzana":
   print(fruit)
