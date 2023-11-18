mi_tupla = (1, 2, 3)
#mi_tupla[1] = 42  # Esto generará un error ya que las tuplas son inmutables

print(mi_tupla)

mi_tupla = mi_tupla + (42,)

print(mi_tupla)
